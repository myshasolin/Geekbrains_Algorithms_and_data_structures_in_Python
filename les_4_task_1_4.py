# Второй вариант
# Найти максимальный элемент среди минимальных элементов столбцов матрицы
# убрал вывод матрицы и прочие принты, в функции задаём размер матрицы
# в этом варианте матрица формируется в цикле for, что делает прогу медлительней - это оч хорошо видно в результатах
# тестов внизу файла

from random import randint
import cProfile


def my_func(size):
    my_matrix, my_list, result = [], [], []

    for i in range(1, (size ** 2) + 1):
        val = randint(1, 100)
        if i % size == 0:
            my_list.append(val)
            my_matrix.append(my_list)
            my_list = []
        else:
            my_list.append(val)
    # print(matrix)

    for num, x in enumerate(range(size)):
        number = 100
        for y in range(size):
            if my_matrix[y][x] < number:
                number = my_matrix[y][x]
        result.append(number)

    result_2 = result[0]
    for i in result:
        if i > result_2:
            result_2 = i
    # print(f'\nМаксимальное число среди минимальных: {result_2}')
    return result_2


# print(my_func(500))
# cProfile.run('my_func(5000)')


# тест при помощи timeit, где N - количество передаваемых на тест элементов - размера матрицы
# python -m timeit -n 1000 -s "import les_4_task_1_4" "les_4_task_1_4.my_func(N)"

# 10x10 матрица)   1000 loops, best of 5: 94.5 usec per loop
# 20x20 матрица)   1000 loops, best of 5: 385 usec per loop
# 50x50 матрица)   1000 loops, best of 5: 2.26 msec per loop
# 100x100 матрица) 1000 loops, best of 5: 9.38 msec per loop
# 500x500 матрица) 1000 loops, best of 5: 240 msec per loop


# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(N)')
# 10x10 матрица)     648 function calls in 0.000 seconds
# 20x20 матрица)     2571 function calls in 0.001 seconds
# 50x50 матрица)     15829 function calls in 0.007 seconds
# 100x100 матрица)   62980 function calls in 0.025 seconds
# 500x500 матрица)   1571146 function calls in 0.592 seconds
# 1000x1000 матрица) 6281924 function calls in 2.188 seconds
# 5000x5000 матрица) 157011893 function calls in 53.609 seconds
