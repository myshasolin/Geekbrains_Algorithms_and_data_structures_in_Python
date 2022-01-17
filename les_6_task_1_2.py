# Второй вариант
# Определить, какое число в массиве встречается чаще всего.
# Решение - при помощи словаря. Сначала генерируем список, потом формируем из него словарь, в котором ключ - это число,
# а значение - кол-во раз, которое это число в списке встречается. Третьим шагом бегаем по сформированному словарю и
# выбираем из него нужный нам ключ по бОльшему значанию, присваиваем цифры переменным, возвращаем строку с результатом

# этот вариант решения по весу тяжелее первого, так как в нём применяется больше переменных

from random import randint
from sum_size import sum_size, operating_system_version


operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def my_func(len_my_list):
    my_list = [randint(1, 8) for i in range(len_my_list)]
    print(my_list)

    diction = {}
    result = number = 0
    for i in my_list:
        if i in diction.keys():
            diction[i] += 1
        else:
            diction[i] = 1
    for x, y in diction.items():
        if y > result:
            number, result = x, y
    print(f'{number} встречается {result} раз ')
    sum_size(len_my_list, my_list, diction, result, number, i, x, y)  # => 1488


my_func(100)

# использовано переменных: 8
# общий их вес: 1448
