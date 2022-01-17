# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Второй — без использования «Решета Эратосфена».

# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2

# мы внутри цикла while крутимся до тех пор, пока итоговый список не будет по длине равен нашему i-му числу. В итоговый
# список мы прибавляем элемент "цифра+1", при этом проверяем - если "цифра+1" делится на элементы списка без остатка,
# то её не добавляем. В результат выводим послений элемент сформированного списка - он и будет нужным нам числом.
# Скорость такого варианта поиска числа, по сравнению с Решетом Эратосфена, гораздо ниже. В ожидании последних замеров
# в 1000 попыток я успел просмотреть 2 серии Игры Престолов, а лучшее время получилось длиной аж 4.69 секунд - всё из-за
# постоянно повторяющегося цикла for с перебором постоянно увеличивающегося списка в постоянно крутящемся while
import cProfile
from functools import lru_cache


# @lru_cache()
def my_func(num):
    result_list, elem_list = [2], 3
    while len(result_list) < num:
        step = True
        for i in result_list.copy():
            if elem_list % i == 0:
                step = False
                break
        if step:
            result_list.append(elem_list)
        elem_list += 1
    return f'{num} это число {result_list[-1]}'


cProfile.run('my_func(10000)')

# answer_num = my_func(int(input('Пиши число вот сюда: ')))
# print(answer_num)


# тест при помощи timeit, где N - количество передаваемых на тест элементов
# python -m timeit -n 1000 -s "import les_4_task_2_2" "les_4_task_2_2.test(N)"

# 10)            1000 loops, best of 5: 9.49 usec per loop
# с @lru_cache() 1000 loops, best of 5: 89.7 nsec per loop

# 20)            1000 loops, best of 5: 28.5 usec per loop
# с @lru_cache() 1000 loops, best of 5: 80.5 nsec per loop

# 50)            1000 loops, best of 5: 128 usec per loop
# с @lru_cache() 1000 loops, best of 5: 81.1 nsec per loop

# 100) 	         1000 loops, best of 5: 459 usec per loop
# с @lru_cache() 1000 loops, best of 5: 88.9 nsec per loop + предупреждение о возможной недостоверности теста

# 500) 	         1000 loops, best of 5: 10.1 msec per loop
# с @lru_cache() 1000 loops, best of 5: 90.7 nsec per loop + предупреждение о возможной недостоверности теста

# 950) 	         1000 loops, best of 5: 37.7 msec per loop
# с @lru_cache() 1000 loops, best of 5: 79.9 nsec per loop + предупреждение о возможной недостоверности теста

# 10000)         1000 loops, best of 5: 4.69 sec per loop
# с @lru_cache() 1000 loops, best of 5: 80.7 nsec per loop + предупреждение о возможной недостоверности теста


# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(N)')
# 10)    68 function calls in 0.001 seconds
#	     28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#	     9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#	     27    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
# 20)    162 function calls in 0.000 seconds
#	     70    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     	 19    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     	 69    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
# 50)    508 function calls in 0.000 seconds
# 	     228    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        49    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        227    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
# 100)   1182 function calls in 0.001 seconds
#        540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        539    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
# 500)   7642 function calls in 0.018 seconds
#        3570    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        3569    0.003    0.000    0.003    0.000 {method 'copy' of 'list' objects}
# 950)   15948 function calls in 0.035 seconds
#        7498    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#        949    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        7497    0.005    0.000    0.005    0.000 {method 'copy' of 'list' objects}
# 10000) 219458 function calls in 4.274 seconds
#        104728    0.011    0.000    0.011    0.000 {built-in method builtins.len}
#        9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#        104727    0.704    0.000    0.704    0.000 {method 'copy' of 'list' objects}
