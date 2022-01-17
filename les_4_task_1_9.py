# Алгоритм Евклида. Третий вариант -  циклический способ, в основе которого остаток от деления. Лучший спобоб из трёх
# представленных,так как здесь нет рекурсии, нет вычитания. Скорость работы максимальная, что видно на одних и всех же
# параметрах тестов для всех трёх вариантов

import cProfile
from functools import lru_cache


# @lru_cache()
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# print(gcd(5555757566574, 247566))

# cProfile.run('gcd(746653536, 366)')

# timeit
# python -m timeit -n 1000 -s "import les_4_task_1_9" "les_4_task_1_9.gcd(746653536, 3663)"
# 1000 loops, best of 5: 649 nsec per loop

# timeit с декоратором @lru_cache()
# 1000 loops, best of 5: 107 nsec per loop

# тест cProfile.run('gcd(746653536, 3663)'):
# 4 function calls in 0.000 seconds

