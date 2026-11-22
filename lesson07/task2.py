# Урок 7. Задание 2 — заменить подряд идущие пробелы одним
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson07

s = input()
while "  " in s:
    s = s.replace("  ", " ")

print(s)
