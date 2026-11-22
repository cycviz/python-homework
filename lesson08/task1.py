# Урок 8. Задание 1 — перевернуть массив

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.reverse()
for x in numbers:
    print(x)
