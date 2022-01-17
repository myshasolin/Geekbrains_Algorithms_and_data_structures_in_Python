# Первый вариант
# Найти максимальный элемент среди минимальных элементов столбцов матрицы
# убрал вывод матрицы и прочие принты, в функции задаём размер матрицы

# этот вариант решения самую малость тяжелее варианта из les_6_task_1_3, т.к. здесь 3 переменны-списка

from random import randint
from sum_size import sum_size, operating_system_version


operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def my_func(size):
    matrix = [[randint(1, 900) for i in range(size)] for _ in range(size)]
    print('наша матрица:')
    for x in matrix:
        for y in x:
            print(f'{y:<5}', end='')
        print()
    print()

    result = []
    for num, xx in enumerate(range(size)):
        number = 100
        for yy in range(size):
            if matrix[yy][xx] < number:
                number = matrix[yy][xx]
        result.append(number)
        print(f'{num + 1} столбец, минимальное число в столбце: {number}')

    result_2 = result[0]
    for ii in result:
        if ii > result_2:
            result_2 = ii
    print(f'\nМаксимальное число среди минимальных: {result_2}')
    sum_size(size, matrix, x, y, result, num, xx, yy, number, result_2, ii)  # => 1640


my_func(50)

# использовано переменных: 11
# общий их вес: 1640
