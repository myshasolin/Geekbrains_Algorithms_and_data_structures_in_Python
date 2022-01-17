# Первый вариант
# Найти максимальный элемент среди минимальных элементов столбцов матрицы
# убрал вывод матрицы и прочие принты, в функции задаём размер матрицы
# этот вариант решения немного быстрее варианта из файла les_4_task_1_4.py в т.ч. за счёт меньшего кол-ва переменных и
# вызовов функции

from random import randint
import cProfile


def my_func(size):
    matrix = [[randint(1, 900) for i in range(size)] for _ in range(size)]
    # print('наша матрица:')
    # for x in matrix:
    #     for y in x:
    #         print(f'{y:<5}', end='')
    #     print()
    # print()

    result = []
    for num, x in enumerate(range(size)):
        number = 100
        for y in range(size):
            if matrix[y][x] < number:
                number = matrix[y][x]
        result.append(number)
        # print(f'{num + 1} столбец, минимальное число в столбце: {number}')

    result_2 = result[0]
    for i in result:
        if i > result_2:
            result_2 = i
    # print(f'\nМаксимальное число среди минимальных: {result_2}')
    return result_2


# print(my_func(500))
# cProfile.run('my_func(5000)')


# тест при помощи timeit, где N - количество передаваемых на тест элементов - размера матрицы
# python -m timeit -n 1000 -s "import les_4_task_1_3" "les_4_task_1_3.my_func(N)"

# 10x10 матрица)   1000 loops, best of 5: 97.1 usec per loop
# 20x20 матрица)   1000 loops, best of 5: 355 usec per loop
# 50x50 матрица)   1000 loops, best of 5: 2.22 msec per loop
# 100x100 матрица) 1000 loops, best of 5: 9.37 msec per loop
# 500x500 матрица) 1000 loops, best of 5: 228 msec per loop

# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(N)')
# 10x10 матрица)     532 function calls in 0.000 seconds
# 20x20 матрица)     2095 function calls in 0.001 seconds
# 50x50 матрица)     12916 function calls in 0.004 seconds
# 100x100 матрица)   51481 function calls in 0.016 seconds
# 500x500 матрица)   1285161 function calls in 0.393 seconds
# 1000x1000 матрица) 5139136 function calls in 1.642 seconds
# 5000x5000 матрица) 128447945 function calls in 42.190 seconds
