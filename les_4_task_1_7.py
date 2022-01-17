# Алгоритм Евклида. Первый вариант решения - простейший арифметический алгоритм, в основе которого вычитание
# Вариант медленный за счёт большого количества проводимых операций
import cProfile
from functools import lru_cache


# @lru_cache()
def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

# print(gcd(5555757566574, 247566))


# cProfile.run('gcd(746653536, 3663)')

# timeit
# python -m timeit -n 1000 -s "import les_4_task_1_7" "les_4_task_1_7.gcd(746653536, 3663)"
# 1000 loops, best of 5: 16.5 msec per loop

# timeit с декоратором @lru_cache()
# 1000 loops, best of 5: 106 nsec per loop + предупреждение о возможной недостоверности теста

# тест cProfile.run('gcd(746653536, 3663)'):
# 4 function calls in 0.024 seconds
