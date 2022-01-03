# Найти максимальный элемент среди минимальных элементов столбцов матрицы
from random import randint

size = 5
matrix = [[randint(1, 90) for i in range(size)] for _ in range(size)]
print('наша матрица:')
for x in matrix:
    for y in x:
        print(f'{y:<5}', end='')
    print()
print()

result = []
for num, x in enumerate(range(size)):
    number = 100
    for y in range(size):
        if matrix[y][x] < number:
            number = matrix[y][x]
    result.append(number)
    print(f'{num + 1} столбец, минимальное число в столбце: {number}')

result_2 = result[0]
for i in result:
    if i > result_2:
        result_2 = i
print(f'\nМаксимальное число среди минимальных: {result_2}')
