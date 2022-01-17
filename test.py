# файл для тестирования кода из les_4_task_2_1.py

import cProfile
import math
from functools import lru_cache


# @lru_cache()
def test(x):
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

    user_answer = x
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
            return f'{x + 1} это число {result_sieve[y]}'


# print(test(20))
# cProfile.run('test(1000000)')
