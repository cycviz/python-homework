# Урок 4. Задание 2 — операции над цифрами пятизначного числа
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson04
# Пример: 46275 -> 7 ** 5 * 2 / (4 - 6) = -16807.0

n = int(input("Пятизначное число: "))

units = n % 10
tens = n // 10 % 10
hundreds = n // 100 % 10
thousands = n // 1000 % 10
ten_thousands = n // 10000 % 10

if ten_thousands == thousands:
    print("Ошибка: разность десятков тысяч и тысяч равна нулю, делить нельзя")
else:
    result = tens ** units * hundreds / (ten_thousands - thousands)
    print(result)
