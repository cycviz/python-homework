"""Игровое поле: деревья, реки, пожары, госпиталь и магазин."""
from utils import randbool, randcell, randcell2
from clouds import CLOUD_TYPES, NONE as NO_CLOUD, THUNDER

# Коды клеток. Индекс в CELL_TYPES = код клетки.
FIELD, TREE, RIVER, HOSPITAL, SHOP, FIRE = range(6)
CELL_TYPES = ["🟩", "🌲", "🌊", "🏥", "🏪", "🔥"]
BORDER = "🟫"
HELICOPTER = "🚁"

TREE_BONUS = 100      # очки за потушенное дерево
BURN_PENALTY = 10     # штраф за сгоревшее дерево
UPGRADE_COST = 500    # +1 к резервуару в магазине
LIFE_COST = 1000      # +10 жизней в госпитале
LIFE_BONUS = 10


class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[FIELD] * w for _ in range(h)]
        self.generate_forest(5, 10)
        for _ in range(max(1, (w * h) // 100)):
            self.generate_river(max(5, (w + h) // 2))
        self.place_building(SHOP)
        self.place_building(HOSPITAL)

    # --- проверки и генерация -------------------------------------------

    def check_bounds(self, x, y):
        """Принадлежит ли клетка (x, y) полю."""
        return 0 <= x < self.w and 0 <= y < self.h

    def generate_river(self, length):
        """Река — случайное блуждание из случайной клетки."""
        x, y = randcell(self.w, self.h)
        self.cells[y][x] = RIVER
        while length > 0:
            x2, y2 = randcell2(x, y)
            if self.check_bounds(x2, y2):
                self.cells[y2][x2] = RIVER
                x, y = x2, y2
                length -= 1

    def generate_forest(self, r, mxr):
        """Каждая клетка поля становится деревом с шансом r/mxr."""
        for y in range(self.h):
            for x in range(self.w):
                if self.cells[y][x] == FIELD and randbool(r, mxr):
                    self.cells[y][x] = TREE

    def generate_tree(self):
        """Вырастить дерево в случайной пустой клетке."""
        x, y = randcell(self.w, self.h)
        if self.cells[y][x] == FIELD:
            self.cells[y][x] = TREE

    def place_building(self, building):
        """Поставить здание в случайную клетку, где нет реки и другого здания."""
        while True:
            x, y = randcell(self.w, self.h)
            if self.cells[y][x] in (FIELD, TREE):
                self.cells[y][x] = building
                return

    def add_fire(self):
        """Поджечь случайную клетку, если там дерево."""
        x, y = randcell(self.w, self.h)
        if self.cells[y][x] == TREE:
            self.cells[y][x] = FIRE

    def update_fires(self, helico):
        """Непотушенные пожары сгорают и перекидываются на соседей, затем — новые пожары."""
        spread = []
        for y in range(self.h):
            for x in range(self.w):
                if self.cells[y][x] == FIRE:
                    self.cells[y][x] = FIELD          # дерево сгорело
                    helico.score -= BURN_PENALTY
                    nx, ny = randcell2(x, y)
                    if self.check_bounds(nx, ny):
                        spread.append((nx, ny))
        for x, y in spread:
            if self.cells[y][x] == TREE:
                self.cells[y][x] = FIRE
        for _ in range(max(3, (self.w * self.h) // 40)):
            self.add_fire()

    # --- взаимодействие с вертолётом -------------------------------------

    def process_helicopter(self, helico, clouds):
        """Что происходит, когда вертолёт прилетел в клетку. Возвращает сообщение."""
        x, y = helico.x, helico.y
        cell = self.cells[y][x]
        msg = ""

        if cell == RIVER:
            helico.tank = helico.mxtank
            msg = "Набрали воды"
        elif cell == FIRE:
            if helico.tank > 0:
                helico.tank -= 1
                helico.score += TREE_BONUS
                self.cells[y][x] = TREE
                msg = f"Пожар потушен! +{TREE_BONUS}"
            else:
                msg = "Нет воды — летите к реке"
        elif cell == SHOP:
            if helico.score >= UPGRADE_COST:
                helico.score -= UPGRADE_COST
                helico.mxtank += 1
                msg = f"Резервуар увеличен до {helico.mxtank}"
            else:
                msg = f"Улучшение стоит {UPGRADE_COST} очков"
        elif cell == HOSPITAL:
            if helico.score >= LIFE_COST:
                helico.score -= LIFE_COST
                helico.lives += LIFE_BONUS
                msg = f"Подлечились: +{LIFE_BONUS} жизней"
            else:
                msg = f"Лечение стоит {LIFE_COST} очков"

        if clouds.cells[y][x] == THUNDER:
            helico.lives -= 1
            msg = "Попали в грозу! −1 жизнь"
        return msg

    # --- отрисовка и сохранение -------------------------------------------

    def draw(self, helico, clouds):
        lines = [BORDER * (self.w + 2)]
        for y in range(self.h):
            line = BORDER
            for x in range(self.w):
                if (x, y) == (helico.x, helico.y):
                    line += HELICOPTER
                elif clouds.cells[y][x] != NO_CLOUD:
                    line += CLOUD_TYPES[clouds.cells[y][x]]
                else:
                    line += CELL_TYPES[self.cells[y][x]]
            lines.append(line + BORDER)
        lines.append(BORDER * (self.w + 2))
        return "\n".join(lines)

    def export_data(self):
        return {"cells": self.cells}

    def import_data(self, data):
        self.cells = data["cells"]
        self.h = len(self.cells)
        self.w = len(self.cells[0])
