# Урок 10. Задание 2 — словарь {n: n ** n} для n от 10 до -5

my_dict = {}
for n in range(10, -6, -1):
    my_dict[n] = n ** n

print(my_dict)
