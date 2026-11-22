# Урок 8. Задание 1 — перевернуть массив
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson08

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.reverse()
for x in numbers:
    print(x)
