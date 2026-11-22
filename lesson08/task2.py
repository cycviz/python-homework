# Урок 8. Задание 2 — циклический сдвиг вправо на 1


def shift_right(arr):
    """Изменяет список на месте: последний элемент встаёт первым."""
    if arr:
        arr.insert(0, arr.pop())


n = int(input())
numbers = list(map(int, input().split()))

shift_right(numbers)
print(*numbers)
