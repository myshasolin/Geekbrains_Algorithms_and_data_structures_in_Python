# Во втором массиве сохранить индексы четных элементов первого массива. Первый вариант решения - вариант с генератором
# внутри локальной функции. В основную функцию в качестве аргумента передаём количество элементов изначального списка
# произвольных чисел. Скорость с @lru_cache() быстрее, результаты тестов ниже. Из трёх вариантов этот самы быстрый.
# Решение, по сути, состоит их двух генераторов - двух строчек кода. Вложенную функцию можно убрать

from random import randint
from functools import lru_cache
import cProfile


# @lru_cache()
def my_func(size):
    my_list = [randint(1, 20) for i in range(size)]

    def _my_func():
        result_list = [x for x, y in enumerate(my_list) if y in my_list and y % 2 == 0]
        return f'список:\n{my_list}\nиндексы чётных чисел:\n{result_list}'
    return _my_func()


# print(my_func(30))
# Profile.run('my_func(1000000)')

# тест при помощи timeit, где N - количество передаваемых на тест элементов
# python -m timeit -n 1000 -s "import les_4_task_1_10" "les_4_task_1_10.my_func(N)"

# 10)            1000 loops, best of 5: 11.8 usec per loop
# с @lru_cache() 1000 loops, best of 5: 85.6 nsec per loop

# 20)            1000 loops, best of 5: 22.2 usec per loop
# с @lru_cache() 1000 loops, best of 5: 81.1 nsec per loop

# 50)            1000 loops, best of 5: 55 usec per loop
# с @lru_cache() 1000 loops, best of 5: 80.3 nsec per loop

# 100) 	         1000 loops, best of 5: 107 usec per loop
# с @lru_cache() 1000 loops, best of 5: 80.4 nsec per loop

# 500) 	         1000 loops, best of 5: 545 usec per loop
# с @lru_cache() 1000 loops, best of 5: 80.3 nsec per loop + предупреждение о возможной недостоверности теста

# 950) 	         1000 loops, best of 5: 1.04 msec per loop
# с @lru_cache() 1000 loops, best of 5: 80.2 nsec per loop + предупреждение о возможной недостоверности теста

# 10000)         1000 loops, best of 5: 10.9 msec per loop
# с @lru_cache() 1000 loops, best of 5: 80 nsec per loop + предупреждение о возможной недостоверности теста


# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(N)')
# 10)      62 function calls in 0.000 seconds
# 	       15    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 20)      114 function calls in 0.000 seconds
# 	       27    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 50)      298 function calls in 0.000 seconds
# 	       91    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 100)     588 function calls in 0.000 seconds
# 	       181    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 500)     2801 function calls in 0.001 seconds
# 	       794    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 950)     5312 function calls in 0.002 seconds
# 	       1505    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 10000)   55985 function calls in 0.023 seconds
# 	       15978    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
# 1000000) 5600433 function calls in 2.306 seconds
# 	       1600426    0.141    0.000    0.141    0.000 {method 'getrandbits' of '_random.Random' objects}

