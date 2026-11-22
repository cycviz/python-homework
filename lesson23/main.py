"""Урок 23. Проект: консольная игра «Вертолёт».

Управление: WASD или стрелки — полёт, F — сохранить, G — загрузить, Q — выход.
Запуск: python3 main.py
"""
import json
import os
import sys
import time

from clouds import Clouds
from helicopter import Helicopter
from keyboard import KeyReader
from map import Map

TICK_SLEEP = 0.05       # длительность тика, сек
TREE_UPDATE = 30        # каждые N тиков вырастает дерево
FIRE_UPDATE = 150       # каждые N тиков: пожары сгорают и появляются новые
CLOUDS_UPDATE = 100     # каждые N тиков меняется погода

SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "save.json")
MOVES = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
MIN_SIZE, MAX_SIZE = 5, 40


class Game:
    def __init__(self, w, h):
        self.field = Map(w, h)
        self.clouds = Clouds(w, h)
        self.helico = Helicopter(w, h)
        self.tick = 1
        self.message = "Тушите пожары! Вода — в реке 🌊"
        self.running = True

    def handle_key(self, key):
        if key in MOVES:
            dx, dy = MOVES[key]
            if self.helico.move(dx, dy):
                msg = self.field.process_helicopter(self.helico, self.clouds)
                if msg:
                    self.message = msg
        elif key == "f":
            self.save()
        elif key == "g":
            self.load()
        elif key == "q":
            self.running = False

    def update(self):
        """Один тик игрового мира."""
        if self.tick % TREE_UPDATE == 0:
            self.field.generate_tree()
        if self.tick % FIRE_UPDATE == 0:
            self.field.update_fires(self.helico)
        if self.tick % CLOUDS_UPDATE == 0:
            self.clouds.update()
        self.tick += 1

    def is_over(self):
        return self.helico.lives <= 0

    def render(self):
        # \033[K — очистить строку до конца, чтобы не оставались хвосты
        # от предыдущего, более длинного сообщения или числа
        return "\033[K\n".join([
            self.helico.stats() + f"   ⏱  {self.tick}",
            self.field.draw(self.helico, self.clouds),
            self.message,
            "WASD/стрелки — полёт · F — сохранить · G — загрузить · Q — выход",
        ])

    # --- сохранение -------------------------------------------------------

    def save(self):
        data = {
            "helicopter": self.helico.export_data(),
            "clouds": self.clouds.export_data(),
            "field": self.field.export_data(),
            "tick": self.tick,
        }
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f)
        self.message = "Игра сохранена 💾"

    def load(self):
        if not os.path.exists(SAVE_FILE):
            self.message = "Сохранения пока нет"
            return
        with open(SAVE_FILE, encoding="utf-8") as f:
            data = json.load(f)
        self.field.import_data(data["field"])
        self.clouds.import_data(data["clouds"])
        self.helico.import_data(data["helicopter"], self.field.w, self.field.h)
        self.tick = data.get("tick", 1)
        self.message = "Игра загружена 📂"


def ask_size(prompt, default):
    while True:
        raw = input(f"{prompt} ({MIN_SIZE}–{MAX_SIZE}, Enter — {default}): ").strip()
        if raw == "":
            return default
        if raw.isdigit() and MIN_SIZE <= int(raw) <= MAX_SIZE:
            return int(raw)
        print("Введите целое число в допустимом диапазоне")


def main():
    if not sys.stdin.isatty():
        print("Запустите игру в терминале: python3 main.py")
        return

    w = ask_size("Ширина поля", 20)
    h = ask_size("Высота поля", 10)
    game = Game(w, h)

    with KeyReader() as keys:
        while game.running and not game.is_over():
            key = keys.get_key()
            if key:
                game.handle_key(key)
            game.update()
            # курсор в начало + кадр + очистка остатка экрана: без мерцания
            sys.stdout.write("\033[H\033[2J" if game.tick == 2 else "\033[H")
            sys.stdout.write(game.render() + "\033[J")
            sys.stdout.flush()
            time.sleep(TICK_SLEEP)

    print()
    if game.is_over():
        print(f"GAME OVER! Жизни закончились. Итоговый счёт: {game.helico.score}")
    else:
        print(f"Выход из игры. Счёт: {game.helico.score}")


if __name__ == "__main__":
    main()
