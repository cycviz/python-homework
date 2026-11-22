# Урок 14. Задание 1 — рекурсивный вывод списка без циклов
# Репозиторий: https://github.com/cycviz/python-homework/tree/main/lesson14

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def print_list(lst, i=0):
    if i == len(lst):
        print("Конец списка")
        return
    print(lst[i])
    print_list(lst, i + 1)


print_list(my_list)
