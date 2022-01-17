# Третий поиска индексов чётных элементов. Этот способ без вложенной функции и без генераторов. В результат собираем
# не список, а конкатенируем строку. Так же передаём количество элементов изначального списка произвольных чисел
# В целом такой вариант работы со строкой медленней двух предыдущих, где мы собирали результат в список.

# по весу аналогичен предыдущему

from random import randint
from sum_size import sum_size, operating_system_version


operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def my_func(size):
    my_list, result = [], ''
    for i in range(size + 1):
        my_list.append(randint(-50, 50))
    for x, y in enumerate(my_list):
        if y % 2 == 0:
            result += f'{x}, '
    print(f'список:\n{my_list}\nиндексы чётных элементов списка:\n{result[0:-2]}')
    print(sum_size(size, my_list, result, i, x, y))


my_func(20)

# использовано переменных: 6
# общий их вес: 461
