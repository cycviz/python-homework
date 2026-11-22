# Урок 6. Задание 1 — сколько нулей среди N чисел
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson06

n = int(input())
zeros = 0
for _ in range(n):
    if int(input()) == 0:
        zeros += 1

print(zeros)
