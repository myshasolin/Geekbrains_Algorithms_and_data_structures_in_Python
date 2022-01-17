# Первый вариант
# Определить, какое число в массиве встречается чаще всего.
# Решение - в функцию передаём длину списка, функция формирует произвольный список и возвращает
# нам число из списка, что встречается в нём больше всего
# этот вариант по скорости чуть медленней, чем вариант со списком из les_4_task_1_2.py в т.ч. за счёт применения count

import cProfile
from random import randint
import functools


def my_func(len_my_list):
    my_list = [randint(1, 8) for i in range(len_my_list)]
    # print(f'список:\n{my_list}')
    result = number = 0
    for i in my_list[:]:
        if my_list.count(i) > result:
            result = my_list.count(i)
            number = i
    # return f'число {number} встречается {result} раз'
    return number, result

# cProfile.run('my_func(1000)')


# тест при помощи timeit, где N - количество передаваемых на тест элементов
# python -m timeit -n 1000 -s "import les_4_task_1_1" "les_4_task_1_1.my_func(N)"
# 10 элементов)   1000 loops, best of 5: 10.7 usec per loop
# с @lru_cache()  1000 loops, best of 5: 79.3 nsec per loop

# 20 элементов)   1000 loops, best of 5: 23.1 usec per loop
# с @lru_cache()  1000 loops, best of 5: 80.5 nsec per loop

# 50 элементов)   1000 loops, best of 5: 73.7 usec per loop
# с @lru_cache()  1000 loops, best of 5: 88.2 nsec per loop

# 100 элементов)  1000 loops, best of 5: 206 usec per loop
# с @lru_cache()  1000 loops, best of 5: 79.5 nsec per loop

# 500 элементов)  1000 loops, best of 5: 3.38 msec per loop
# с @lru_cache()  1000 loops, best of 5: 82 nsec per loop + предупреждение о возможной недостоверности теста

# 1000 элементов) 1000 loops, best of 5: 12.8 msec per loop
# с @lru_cache()  1000 loops, best of 5: 81.6 nsec per loop + предупреждение о возможной недостоверности теста

# 10000 элементов) 1000 loops, best of 5: 12.8 msec per loop
# с @lru_cache()   1000 loops, best of 5: 80.6 nsec per loop + предупреждение о возможной недостоверности теста


# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(N)')
# 10 элементов)   83 function calls in 0.000 seconds
# 		          11    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
# 		          21    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 20 элементов)   138 function calls in 0.000 seconds
# 		          23    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
# 		          32    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 50 элементов)   346 function calls in 0.000 seconds
# 		          52    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
# 		          89    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 100 элементов)  719 function calls in 0.000 seconds
# 		          103    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
# 		          211    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 500 элементов)  3530 function calls in 0.004 seconds
# 		          502    0.003    0.000    0.003    0.000 {method 'count' of 'list' objects}
# 		          1023    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 1000 элементоа) 7017 function calls in 0.014 seconds
# 		          1002    0.012    0.000    0.012    0.000 {method 'count' of 'list' objects}
# 		          2010    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}








