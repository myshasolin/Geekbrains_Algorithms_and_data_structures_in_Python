# Второй вариант
# Определить, какое число в массиве встречается чаще всего.
# Решение - при помощи словаря. Сначала генерируем список, потом формируем из него словарь, в котором ключ - это число,
# а значение - кол-во раз, которое это число в списке встречается. Третьим шагом бегаем по сформированному словарю и
# выбираем из него нужный нам ключ по бОльшему значанию, присваиваем цифры переменным, возвращаем строку с результатом
# этот вариант решения по скорости лучше, чем вариант со списком из les_4_task_1_1.py, это видно по timeit'
# показатели плюс/минус одинаковые

import cProfile
from random import randint
import functools


# @functools.lru_cache()
def my_func(len_my_list):
    my_list = [randint(1, 8) for i in range(len_my_list)]
    # print(my_list)

    diction = {}
    result = number = 0
    for i in my_list:
        if i in diction.keys():
            diction[i] += 1
        else:
            diction[i] = 1
    for x, y in diction.items():
        if y > result:
            number, result = x, y

    return f'{number} встречается {result} раз '


# cProfile.run('my_func(1000)')

# тест при помощи timeit, где N - количество передаваемых на тест элементов
# python -m timeit -n 1000 -s "import les_4_task_1_2" "les_4_task_1_2.my_func(N)"
# 10 элементов)    1000 loops, best of 5: 10.7 usec per loop
# с @lru_cache()   1000 loops, best of 5: 80.9 nsec per loop

# 20 элементов)    1000 loops, best of 5: 20.1 usec per loop
# с @lru_cache()   1000 loops, best of 5: 82.3 nsec per loop

# 50 элементов)    1000 loops, best of 5: 47.8 usec per loop
# с @lru_cache()   1000 loops, best of 5: 79.9 nsec per loop

# 100 элементов)   1000 loops, best of 5: 94.7 usec per loop
# с @lru_cache()   1000 loops, best of 5: 78.2 nsec per loop

# 500 элементов)   1000 loops, best of 5: 484 usec per loop
# с @lru_cache()   1000 loops, best of 5: 81.5 nsec per loop + предупреждение о возможной недостоверности теста

# 1000 элементов)  1000 loops, best of 5: 974 usec per loop
# с @lru_cache()   1000 loops, best of 5: 84.2 nsec per loop + предупреждение о возможной недостоверности теста

# 10000 элементов) 1000 loops, best of 5: 9.83 msec per loop
# с @lru_cache()   1000 loops, best of 5: 80 nsec per loop + предупреждение о возможной недостоверности теста


# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(N)')
# 10 элементов)   77 function calls in 0.000 seconds
# 		          21    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 20 элементов)   152 function calls in 0.000 seconds
# 		          46    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 50 элементов)   349 function calls in 0.000 seconds
# 		          93    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 100 элементов)  694 function calls in 0.000 seconds
#		          188    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 500 элементов)  3536 function calls in 0.001 seconds
# 		          1030    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 1000 элементоа) 6990 function calls in 0.004 seconds
# 		          1984    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
