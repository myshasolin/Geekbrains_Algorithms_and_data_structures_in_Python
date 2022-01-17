# Второй вариант
# Найти максимальный элемент среди минимальных элементов столбцов матрицы
# убрал вывод матрицы и прочие принты, в функции задаём размер матрицы

# в плане производительности этот вариант программы медленнее, а вот по весу чуть легче предудыщего, несмотря на +2
# переменных, так как мы по матрице бегаем чуть меньше и у нас 2 переменных-списка (в первом варианте их 3)

from random import randint
from sum_size import sum_size, operating_system_version


operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def my_func(size):
    my_matrix, my_list, result = [], [], []
    size2 = size ** 2

    for i in range(1, size2 + 1):
        val = randint(1, 100)
        if i % size == 0:
            my_list.append(val)
            my_matrix.append(my_list)
            my_list = []
        else:
            my_list.append(val)
    print(my_matrix)

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
    print(f'\nМаксимальное число среди минимальных: {result_2}')
    sum_size(size, my_matrix, my_list, result, i, size2, 1, val, num, x, number, y, result_2)  # => 1280


my_func(50)

# использовано переменных: 13
# общий их вес: 1280
