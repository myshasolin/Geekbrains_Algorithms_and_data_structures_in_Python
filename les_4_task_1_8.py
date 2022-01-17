# Алгоритм Евклида. Второй вариант - рекурсивный поиск, основанный на остатке от деления. Лучше варианта с вычитанием
# но у этого варианта есть ограничения по стеку памяти вызова функции. В скорости он существенно уступает третьему
# способу из les_4_task_1_9.py
# - тесты ниже это показывают и доказывают

import cProfile
from functools import lru_cache


# @lru_cache()
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# print(gcd(5555757566574, 247566))


# cProfile.run('gcd(746653536, 366)')

# timeit
# python -m timeit -n 1000 -s "import les_4_task_1_8" "les_4_task_1_8.gcd(746653536, 3663)"
# 1000 loops, best of 5: 1.06 usec per loop

# timeit с декоратором @lru_cache()
# 1000 loops, best of 5: 108 nsec per loop

# тест cProfile.run('gcd(746653536, 3663)'):
# 12 function calls (4 primitive calls) in 0.000 seconds
