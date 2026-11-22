# Урок 6. Задание 3 — чётные числа на отрезке [A, B]
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson06

a = int(input())
b = int(input())

start = a if a % 2 == 0 else a + 1
evens = []
for n in range(start, b + 1, 2):
    evens.append(str(n))

print(" ".join(evens))
