"""Вертолёт игрока."""
from utils import randcell


class Helicopter:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.x, self.y = randcell(w, h)
        self.tank = 0        # сколько воды сейчас
        self.mxtank = 1      # вместимость резервуара
        self.score = 0
        self.lives = 20

    def move(self, dx, dy):
        """Сдвинуться, если не вылетаем за поле. Возвращает True, если сдвинулись."""
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < self.w and 0 <= ny < self.h:
            self.x, self.y = nx, ny
            return True
        return False

    def stats(self):
        return (f"💧 {self.tank}/{self.mxtank}   "
                f"🏆 {self.score}   "
                f"💛 {self.lives}")

    def export_data(self):
        return {
            "x": self.x, "y": self.y,
            "tank": self.tank, "mxtank": self.mxtank,
            "score": self.score, "lives": self.lives,
        }

    def import_data(self, data, w, h):
        self.w, self.h = w, h
        self.x = data["x"]
        self.y = data["y"]
        self.tank = data["tank"]
        self.mxtank = data["mxtank"]
        self.score = data["score"]
        self.lives = data["lives"]
