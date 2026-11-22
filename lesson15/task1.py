# Урок 15. Задание 1 — наследование
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson15


class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Autobus(Transport):
    pass


bus = Autobus("Renaul Logan", 180, 12)
print(f"Название автомобиля: {bus.name} Скорость: {bus.max_speed} Пробег: {bus.mileage}")
