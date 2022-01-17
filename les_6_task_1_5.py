# рекурсивная функция, возвращающая строку цифр от a до b. Первый вариант решения. Этот вариант программы медленнее
# способа, формирующего строку в генераторе + имеет ограничения стека памяти

# программа простейшая и вес такой же

from sum_size import sum_size, operating_system_version


operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def my_func(a, b, sum_plus=1):
    if sum_plus:
        return sum_size(a, b)
    if a == b:
        return a
    elif a > b:
        return f'{a}, {my_func(a - 1, b)}'
    return f'{a}, {my_func(a + 1, b)}'


my_func(50, 0)

# использовано переменных: 2
# общий их вес: 52
