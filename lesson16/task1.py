# Урок 16. Задание 1 — класс Касса


class CashRegister:
    def __init__(self, money=0):
        self.money = money

    def top_up(self, x):
        self.money += x

    def count_1000(self):
        print(self.money // 1000)

    def take_away(self, x):
        if x > self.money:
            raise ValueError("Недостаточно денег в кассе")
        self.money -= x


if __name__ == "__main__":
    cash = CashRegister()
    cash.top_up(5500)
    cash.count_1000()        # 5
    cash.take_away(2000)
    cash.count_1000()        # 3
    try:
        cash.take_away(10000)
    except ValueError as e:
        print("Ошибка:", e)
