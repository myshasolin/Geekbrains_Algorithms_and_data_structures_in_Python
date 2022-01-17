# Второй вариант поиска индексов чётных элементов, этот вариант без вложенной функции и без генераторов.
# Так же передаём количество элементов изначального списка произвольных чисел
# скорость с @lru_cache() быстрее

# по скорости это решение на больших значениях (в примере N = 1000000) полегче предыдущего, т.к. нет внутренней функции

from random import randint
from sum_size import sum_size, operating_system_version


operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def my_func(size):
    my_list, result = [], []
    for i in range(size + 1):
        my_list.append(randint(-50, 50))
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            result.append(i)
    print(f'список:\n{my_list}\nиндексы чётных элементов списка:\n{result}')
    sum_size(size, my_list, result, i)


my_func(20)

# использовано переменных: 4
# общий их вес: 488
