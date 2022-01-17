# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».

# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2

# Решетом Эратосфена мы формируем список простых чисел. Для нахождения i-го простого числа в сформированном списке мы
# должны иметь список нужной длины, из которого уже в цикле мы вытаскиваем нужное нам число по совпадению его индекса с
# желаемым числом. Мойжно пойти двумя путями:
# 1) Ограничить диапазон возможных задаваемых чисел
# 2) Вычислять длину решета по теореме распределения простых чисел, согласно которой количество простых чисел на
# отрезке [1;n] растёт с увеличением n как n/log(n). Но и при таком варианте важно учесть исключение, возникающее
# если при условии, что i-тое число = 2
# итого сначала мы формируем число под решето, потом само решето, потом бегаем в цикле по решету - тесты скорости
# говорят сами за себя, они выше, чем в варианте поиска числа без решета, несмотря на то, что модуль math съедает
# много времени. Этот вариант предпочтительней.
# Для тестов загнал код в отдельную функцию и убрал из него все инпуты и принты. Код для теста лежит в test.py
import math


def the_range_of_the_sieve_of_eratosthenes(num):
    step, number = 0, 2
    if num == 2:
        number = 4
        return number
    else:
        while step <= num:
            step = number / math.log(number)
            number += 1
        return number


user_answer = int(input('какое найдём простое число? Пиши здесь число: '))
spam = the_range_of_the_sieve_of_eratosthenes(user_answer)

sieve = [i for i in range(spam)]
sieve[1] = 0
for i in range(2, spam):
    if sieve[i] != 0:
        j = i * 2
        while j < spam:
            sieve[j] = 0
            j += i

result_sieve = [i for i in sieve if i != 0]

for x, y in enumerate(range(len(result_sieve))):
    if user_answer == x + 1:
        print(f'{x + 1} это число {result_sieve[y]}')


# тест при помощи timeit, где N - количество передаваемых на тест элементов
# python -m timeit -n 1000 -s "import test" "test.test(N)"

# 10)            1000 loops, best of 5: 17.3 usec per loop
# с @lru_cache() 1000 loops, best of 5: 81.1 nsec per loop

# 20)            1000 loops, best of 5: 41.1 usec per loop
# с @lru_cache() 1000 loops, best of 5: 80.7 nsec per loop

# 50)            1000 loops, best of 5: 134 usec per loop
# с @lru_cache() 1000 loops, best of 5: 83 nsec per loop

# 100) 	         1000 loops, best of 5: 338 usec per loop
# с @lru_cache() 1000 loops, best of 5: 84 nsec per loop + предупреждение о возможной недостоверности теста

# 500) 	         1000 loops, best of 5: 2.27 msec per loop
# с @lru_cache() 1000 loops, best of 5: 83.2 nsec per loop + предупреждение о возможной недостоверности теста

# 950) 	         1000 loops, best of 5: 4.79 msec per loop
# с @lru_cache() 1000 loops, best of 5: 80.1 nsec per loop + предупреждение о возможной недостоверности теста

# 10000)         1000 loops, best of 5: 71.2 msec per loop
# с @lru_cache() 1000 loops, best of 5: 83 nsec per loop + предупреждение о возможной недостоверности теста


# тест при помощи cProfile, где N - количество передаваемых на тест элементов
# cProfile.run('my_func(N)')
# 10)      43 function calls in 0.000 seconds
# 	       35    0.000    0.000    0.000    0.000 {built-in method math.log}
# 20)      97 function calls in 0.000 seconds
# 	       89    0.000    0.000    0.000    0.000 {built-in method math.log}
# 50)      290 function calls in 0.000 seconds
# 	       282    0.000    0.000    0.000    0.000 {built-in method math.log}
# 100)     655 function calls in 0.001 seconds
# 	       647    0.000    0.000    0.000    0.000 {built-in method math.log}
# 500)     4175 function calls in 0.003 seconds
# 	       4167    0.001    0.000    0.001    0.000 {built-in method math.log}
# 950)     8615 function calls in 0.005 seconds
# 	       8607    0.001    0.000    0.001    0.000 {built-in method math.log}
# 10000)   116679 function calls in 0.080 seconds
# 	       116671    0.016    0.000    0.016    0.000 {built-in method math.log}
# 1000000) 16626516 function calls in 15.790 seconds
# 	       16626508    2.194    0.000    2.194    0.000 {built-in method math.log}
