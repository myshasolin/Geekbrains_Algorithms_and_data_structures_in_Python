# Третий поиска индексов чётных элементов. Этот способ без вложенной функции и без генераторов. В результат собираем
# не список, а конкатенируем строку. Так же передаём количество элементов изначального списка произвольных чисел
# В целом такой вариант работы со строкой медленней двух предыдущих, где мы собирали результат в список.
# Скорость с @lru_cache() так же быстрее, результаты тестов ниже

from random import randint
from functools import lru_cache
import cProfile


# @lru_cache()
def my_func(size):
    my_list, result = [], ''
    for i in range(size + 1):
        my_list.append(randint(-50, 50))
    for x, y in enumerate(my_list):
        if y % 2 == 0:
            result += f'{x}, '
    return f'список:\n{my_list}\nиндексы чётных элементов списка:\n{result[0:-2]}'


# print(my_func(20))
# cProfile.run('my_func(10000000)')


# тест при помощи timeit, где N - количество передаваемых на тест элементов
# python -m timeit -n 1000 -s "import les_4_task_1_12" "les_4_task_1_12.my_func(N)"

# 10)            1000 loops, best of 5: 12.5 usec per loop
# с @lru_cache() 1000 loops, best of 5: 81.2 nsec per loop

# 20)            1000 loops, best of 5: 22.4 usec per loop
# с @lru_cache() 1000 loops, best of 5: 80.9 nsec per loop

# 50)            1000 loops, best of 5: 51.6 usec per loop
# с @lru_cache() 1000 loops, best of 5: 79.9 nsec per loop

# 100) 	         1000 loops, best of 5: 101 usec per loop
# с @lru_cache() 1000 loops, best of 5: 83.6 nsec per loop

# 500) 	         1000 loops, best of 5: 531 usec per loop
# с @lru_cache() 1000 loops, best of 5: 79.9 nsec per loop + предупреждение о возможной недостоверности теста

# 950) 	         1000 loops, best of 5: 1 msec per loop
# с @lru_cache() 1000 loops, best of 5: 80.6 nsec per loop + предупреждение о возможной недостоверности теста

# 10000)         1000 loops, best of 5: 10.2 msec per loop
# с @lru_cache() 1000 loops, best of 5: 83.6 nsec per loop + предупреждение о возможной недостоверности теста


# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(N)')
# 10)       74 function calls in 0.000 seconds
# 	        15    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 20)       136 function calls in 0.000 seconds
# 	        27    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 50)       326 function calls in 0.000 seconds
# 	        67    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 100)      631 function calls in 0.000 seconds
# 	        122    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 500)      3157 function calls in 0.001 seconds
# 	        648    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 950)      5948 function calls in 0.002 seconds
# 	        1189    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 10000)    62616 function calls in 0.022 seconds
# 	        12607    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
# 1000000)  6266994 function calls in 2.791 seconds
# 	        1266985    0.118    0.000    0.118    0.000 {method 'getrandbits' of '_random.Random' objects}
# 10000000) 62671781 function calls in 81.353 seconds
# 	        12671772    1.155    0.000    1.155    0.000 {method 'getrandbits' of '_random.Random' objects}
