# Второй вариант поиска индексов чётных элементов, этот вариант без вложенной функции и без генераторов.
# Так же передаём количество элементов изначального списка произвольных чисел
# скорость с @lru_cache() быстрее, но в целом по скорости это решение на больших значениях (в примере N = 1000000)
# немного уступает первому решению из les_4_task_1_11.py, результаты тестов ниже

from random import randint
from functools import lru_cache
import cProfile


# @lru_cache()
def my_func(size):
    my_list, result = [], []
    for i in range(size + 1):
        my_list.append(randint(-50, 50))
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            result.append(i)
    return f'список:\n{my_list}\nиндексы чётных элементов списка:\n{result}'


# print(my_func(20))
# cProfile.run('my_func(1000000)')


# тест при помощи timeit, где N - количество передаваемых на тест элементов
# python -m timeit -n 1000 -s "import les_4_task_1_11 "les_4_task_1_11.my_func(N)"

# 10)            1000 loops, best of 5: 11 usec per loop
# с @lru_cache() 1000 loops, best of 5: 81 nsec per loop

# 20)            1000 loops, best of 5: 20.9 usec per loop
# с @lru_cache() 1000 loops, best of 5: 82 nsec per loop

# 50)            1000 loops, best of 5: 49.6 usec per loop
# с @lru_cache() 1000 loops, best of 5: 82.5 nsec per loop

# 100) 	         1000 loops, best of 5: 96.7 usec per loop
# с @lru_cache() 1000 loops, best of 5: 81.7 nsec per loop

# 500) 	         1000 loops, best of 5: 497 usec per loop
# с @lru_cache() 1000 loops, best of 5: 81.2 nsec per loop + предупреждение о возможной недостоверности теста

# 950) 	         1000 loops, best of 5: 924 usec per loop
# с @lru_cache() 1000 loops, best of 5: 79.3 nsec per loop + предупреждение о возможной недостоверности теста

# 10000)         1000 loops, best of 5: 10.6 msec per loop
# с @lru_cache() 1000 loops, best of 5: 81.3 nsec per loop + предупреждение о возможной недостоверности теста


# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(N)')
# 10)      64 function calls in 0.000 seconds
# 	       15    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 20)      123 function calls in 0.000 seconds
# 	       26    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 50)      291 function calls in 0.000 seconds
# 	       60    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 100)     579 function calls in 0.000 seconds
# 	       129    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 500)     2883 function calls in 0.001 seconds
# 	       624    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 950)     5482 function calls in 0.002 seconds
# 	       1199    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 10000)   57731 function calls in 0.021 seconds
# 	       12575    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
# 1000000) 6773139 function calls in 2.437 seconds
# 	       1267623    0.113    0.000    0.113    0.000 {method 'getrandbits' of '_random.Random' objects}
