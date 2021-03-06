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

# по весу увесистая программа. Ну оно и понятно, решето же

import math
from sum_size import sum_size, operating_system_version

operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


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


# user_answer = int(input('какое найдём простое число? Пиши здесь число: '))
user_answer = 30
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

sum_size(user_answer, spam, sieve, sieve[1], i, j, result_sieve, x, y, the_range_of_the_sieve_of_eratosthenes)

# использовано переменных: 10
# общий их вес: 2136
