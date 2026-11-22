# Урок 11. Задание 1 — список факториалов
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson11
# 3 -> 3! = 6 -> [6!, 5!, 4!, 3!, 2!, 1!] = [720, 120, 24, 6, 2, 1]


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


n = int(input("Натуральное число: "))
f = factorial(n)
print(f"{n}! = {f}")

factorials = [factorial(i) for i in range(f, 0, -1)]
print(factorials)
