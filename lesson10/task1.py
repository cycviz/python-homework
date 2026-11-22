# Урок 10. Задание 1 — словарь питомцев

pets = {}

name = input("Кличка питомца: ")
species = input("Вид питомца: ")
age = int(input("Возраст питомца: "))
owner = input("Имя владельца: ")

pets[name] = {
    "Вид питомца": species,
    "Возраст питомца": age,
    "Имя владельца": owner,
}

# Склонение: 1, 21, 31 -> год; 2-4, 22-24 -> года; 5-20, 11-14 -> лет
if 11 <= age % 100 <= 14:
    suffix = "лет"
elif age % 10 == 1:
    suffix = "год"
elif 2 <= age % 10 <= 4:
    suffix = "года"
else:
    suffix = "лет"

for pet_name in pets.keys():
    species, age, owner = pets[pet_name].values()
    print(f'Это {species} по кличке "{pet_name}". '
          f'Возраст питомца: {age} {suffix}. Имя владельца: {owner}')
