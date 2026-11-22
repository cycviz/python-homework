# Урок 13. Задание 1 — генерация и сложение матриц
import random


def generate_matrix(rows, cols, low=-100, high=100):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(random.randint(low, high))
        matrix.append(row)
    return matrix


def add_matrices(m1, m2):
    if len(m1) != len(m2) or any(len(r1) != len(r2) for r1, r2 in zip(m1, m2)):
        raise ValueError("Складывать можно только матрицы одинаковой размерности")
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{x:5}" for x in row))


rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))

matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)
matrix_3 = add_matrices(matrix_1, matrix_2)

print("\nmatrix_1:")
print_matrix(matrix_1)
print("\nmatrix_2:")
print_matrix(matrix_2)
print("\nmatrix_3 = matrix_1 + matrix_2:")
print_matrix(matrix_3)
