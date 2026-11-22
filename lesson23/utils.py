"""Вспомогательные функции случайной генерации."""
import random


def randbool(r, mxr):
    """True с вероятностью r / mxr."""
    return random.randint(1, mxr) <= r


def randcell(w, h):
    """Случайная клетка поля w x h: координаты (x, y)."""
    return random.randint(0, w - 1), random.randint(0, h - 1)


def randcell2(x, y):
    """Случайная соседняя клетка (вверх/вниз/влево/вправо)."""
    dx, dy = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
    return x + dx, y + dy
