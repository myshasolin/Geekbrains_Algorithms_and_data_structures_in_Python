# Определить, какое число в массиве встречается чаще всего.
# Решение - в функцию передаём длину списка, функция формирует произвольный список и возвращает
# нам число из списка, что встречается в нём больше всего

# этот вариант по весу легче второго, т.к. в нём используется меньше переменных

from random import randint
from sum_size import sum_size, operating_system_version


operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def my_func(size):
    my_list = [randint(1, 8) for i in range(size)]
    print(f'список:\n{my_list}')
    result = number = 0
    for i in my_list[:]:
        if my_list.count(i) > result:
            result = my_list.count(i)
            number = i
    print(f'число {number} встречается {result} раз')
    sum_size(my_list, result, number, size, i)  # => 1032


my_func(100)

# использовано переменных: 5
# общий их вес: 1032
