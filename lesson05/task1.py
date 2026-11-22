# Урок 5. Задание 1 — описание числа
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson05

n = int(input("Целое число: "))

if n == 0:
    print("нулевое число")
else:
    sign = "положительное" if n > 0 else "отрицательное"
    parity = "четное" if n % 2 == 0 else "нечетное"
    print(f"{sign} {parity} число")
    if n % 2 != 0:
        print("число не является четным")
