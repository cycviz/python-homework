"""Погода: облака и грозы."""
from utils import randbool

NONE, CLOUD, THUNDER = 0, 1, 2
CLOUD_TYPES = {CLOUD: "💭", THUNDER: "🌀"}


class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[NONE] * w for _ in range(h)]

    def update(self, r=1, mxr=20, g=1, mxg=10):
        """Перегенерировать погоду.

        Клетка становится облаком с шансом r/mxr,
        а облако — грозой с шансом g/mxg.
        """
        for y in range(self.h):
            for x in range(self.w):
                if randbool(r, mxr):
                    self.cells[y][x] = THUNDER if randbool(g, mxg) else CLOUD
                else:
                    self.cells[y][x] = NONE

    def export_data(self):
        return {"cells": self.cells}

    def import_data(self, data):
        self.cells = data["cells"]
        self.h = len(self.cells)
        self.w = len(self.cells[0])
