# Урок 11. Задание 2 — "база данных" ветклиники (CRUD)
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson11
import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел",
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша",
        },
    },
}


def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False


def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    if age % 10 == 1:
        return "год"
    if 2 <= age % 10 <= 4:
        return "года"
    return "лет"


def input_pet_info():
    name = input("Кличка питомца: ")
    species = input("Вид питомца: ")
    age = int(input("Возраст питомца: "))
    owner = input("Имя владельца: ")
    return {name: {"Вид питомца": species,
                   "Возраст питомца": age,
                   "Имя владельца": owner}}


def input_id():
    value = input("ID питомца: ")
    return int(value) if value.isdigit() else None


def format_pet(pet):
    name = list(pet.keys())[0]
    info = pet[name]
    age = info["Возраст питомца"]
    return (f'Это {info["Вид питомца"]} по кличке "{name}". '
            f'Возраст питомца: {age} {get_suffix(age)}. '
            f'Имя владельца: {info["Имя владельца"]}')


def create():
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    pets[last + 1] = input_pet_info()
    print(f"Питомец добавлен с ID {last + 1}")


def read():
    pet = get_pet(input_id())
    print(format_pet(pet) if pet else "Питомец с таким ID не найден")


def update():
    ID = input_id()
    if get_pet(ID):
        pets[ID] = input_pet_info()
        print("Запись обновлена")
    else:
        print("Питомец с таким ID не найден")


def delete():
    ID = input_id()
    if get_pet(ID):
        del pets[ID]
        print("Запись удалена")
    else:
        print("Питомец с таким ID не найден")


def pets_list():
    if not pets:
        print("База пуста")
    for ID, pet in pets.items():
        print(f"{ID}: {format_pet(pet)}")


commands = {
    "create": create,
    "read": read,
    "update": update,
    "delete": delete,
    "list": pets_list,
}

command = ""
while command != "stop":
    command = input("\nКоманда (create/read/update/delete/list/stop): ").strip()
    if command in commands:
        commands[command]()
    elif command != "stop":
        print("Неизвестная команда")
