# рекурсивная функция, возвращающая строку цифр от a до b. Первый вариант решения. Этот вариант программы медленнее
# способа, формирующего строку в генераторе + имеет ограничения стека памяти

import cProfile
import functools


# @functools.lru_cache()
def my_func(a, b):
    if a == b:
        return a
    elif a > b:
        return f'{a}, {my_func(a - 1, b)}'
    return f'{a}, {my_func(a + 1, b)}'


# print(my_func(8, 2))
# cProfile.run('my_func(1, 400)')


# тест при помощи timeit, где N - количество передаваемых на тест элементов
# python -m timeit -n 1000 -s "import les_4_task_1_5" "les_4_task_1_5.my_func(1, N)"

# 10)   	  1000 loops, best of 5: 2.65 usec per loop
# с @lru_cache()  1000 loops, best of 5: 112 nsec per loop

# 20)   	  1000 loops, best of 5: 5.5 usec per loop
# с @lru_cache()  1000 loops, best of 5: 106 nsec per loop

# 50)   	  1000 loops, best of 5: 13.7 usec per loop
# с @lru_cache()  1000 loops, best of 5: 104 nsec per loop

# 100) 	  	  1000 loops, best of 5: 27.3 usec per loop
# с @lru_cache()  1000 loops, best of 5: 106 nsec per loop

# 500) 		  1000 loops, best of 5: 225 usec per loop
# с @lru_cache()  уже превышение: RecursionError: maximum recursion depth exceeded in comparison

# 950) 1000 loops, best of 5: 473 usec per loop
# Дальше уже превышение: RecursionError: maximum recursion depth exceeded in comparison


# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(1, N)')
# 10)  10/1    0.000    0.000    0.000    0.000 les_4_task_1_4.py:5(my_func)
# 20)  20/1    0.000    0.000    0.000    0.000 les_4_task_1_4.py:5(my_func)
# 50)  50/1    0.000    0.000    0.000    0.000 les_4_task_1_4.py:5(my_func)
# 100) 100/1    0.000    0.000    0.000    0.000 les_4_task_1_4.py:5(my_func)
# 500) 500/1    0.001    0.000    0.001    0.001 les_4_task_1_4.py:5(my_func)
# 950) 950/1    0.002    0.000    0.002    0.002 les_4_task_1_4.py:5(my_func)
# 990) 990/1    0.002    0.000    0.002    0.002 les_4_task_1_4.py:5(my_func)
# Дальше уже превышение: RecursionError: maximum recursion depth exceeded in comparison
