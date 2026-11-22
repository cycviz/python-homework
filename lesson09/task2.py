# Урок 9. Задание 2 — сколько чисел есть в обоих списках

first = set(map(int, input().split()))
second = set(map(int, input().split()))
print(len(first & second))
