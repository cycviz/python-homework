# Урок 16. Задание 2 — класс Черепашка
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson16
# В условии go_right() "увеличивает y" — опечатка: вправо меняется x.


class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s - 1 <= 0:
            raise ValueError("Шаг черепашки не может стать <= 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        """Минимум ходов до (x2, y2) с текущим шагом s.

        Ходы по осям независимы, поэтому ответ — |dx| / s + |dy| / s.
        Если расстояние по какой-то оси не делится на s, точка недостижима
        при текущем шаге — выбрасываем ошибку.
        """
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        if dx % self.s != 0 or dy % self.s != 0:
            raise ValueError(f"Точка ({x2}, {y2}) недостижима с шагом {self.s}")
        return dx // self.s + dy // self.s


if __name__ == "__main__":
    t = Turtle()
    t.evolve()                   # s = 2
    t.go_right()
    t.go_up()
    print(t.x, t.y, t.s)         # 2 2 2
    print(t.count_moves(8, -4))  # 3 + 3 = 6
    try:
        t.count_moves(3, 0)
    except ValueError as e:
        print("Ошибка:", e)
