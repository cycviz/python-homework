# Урок 7. Задание 2 — заменить подряд идущие пробелы одним

s = input()
while "  " in s:
    s = s.replace("  ", " ")

print(s)
