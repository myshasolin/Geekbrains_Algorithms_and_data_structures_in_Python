# функция, формирующая в генераторе и возвращающая строку от a до b
# Второй вариант решения. этот способ в разы быстрее рекурсивной функции + не имеет ограничений стека памяти в 1000.
# Последовательность от 1 до 10 млн. сформировалась в миг
import cProfile


def my_func(a, b):
    if a < b:
        my_list = [i for i in range(a, b + 1)]
        return str(my_list)[1:-1]
    elif a > b:
        my_list = [i for i in range(a, b - 1, -1)]
        return str(my_list)[1:-1]

# print(my_func(50, 33))
# cProfile.run('my_func(1, 10000000)')

# тест при помощи timeit, где N - количество передаваемых на тест элементов
# python -m timeit -n 1000 -s "import les_4_task_1_4" "les_4_task_1_4.my_func(1, N)"

# 10)     1000 loops, best of 5: 2.33 usec per loop
# 20)     1000 loops, best of 5: 2.67 usec per loop
# 50)     1000 loops, best of 5: 5.41 usec per loop
# 100) 	  1000 loops, best of 5: 10.1 usec per loop
# 500) 	  1000 loops, best of 5: 50.9 usec per loop
# 950) 	  1000 loops, best of 5: 99.1 usec per loop
# 100000) 1000 loops, best of 5: 12.6 msec per loop


# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(1, N)')
# число от 1 до 10 млн. за: 5 function calls in 1.583 seconds
# и никаких ограничений стека памяти
