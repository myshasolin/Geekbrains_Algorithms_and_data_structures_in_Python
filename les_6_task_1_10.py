# Во втором массиве сохранить индексы четных элементов первого массива. Первый вариант решения - вариант с генератором
# внутри локальной функции. В основную функцию в качестве аргумента передаём количество элементов изначального списка
# произвольных чисел. Скорость с @lru_cache() быстрее, результаты тестов ниже. Из трёх вариантов этот самы быстрый.
# Решение, по сути, состоит их двух генераторов - двух строчек кода. Вложенную функцию можно убрать

# За счёт внутренней функции он ещё и потяженее, чет код les_6_task_1_11

from random import randint
from sum_size import sum_size, operating_system_version


operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def my_func(size):
    my_list = [randint(1, 20) for i in range(size)]
    def _my_func():
        result_list = [x for x, y in enumerate(my_list) if y in my_list and y % 2 == 0]
        print(f'список:\n{my_list}\nиндексы чётных чисел:\n{result_list}')
        print(sum_size(size, my_list, result_list, _my_func))
    print(_my_func())


my_func(30)

# использовано переменных: 4
# общий их вес: 724
