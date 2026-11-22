# Урок 9. Задание 2 — сколько чисел есть в обоих списках
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson09

first = set(map(int, input().split()))
second = set(map(int, input().split()))
print(len(first & second))
