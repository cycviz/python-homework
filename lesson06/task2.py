# Урок 6. Задание 2 — количество делителей числа X (X <= 2e9)
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson06
# Перебираем делители только до корня из X: каждый делитель i < sqrt(X)
# имеет пару X // i. Иначе 2 млрд итераций выполнялись бы минуты.

x = int(input())

count = 0
i = 1
while i * i <= x:
    if x % i == 0:
        count += 1 if i * i == x else 2
    i += 1

print(count)
