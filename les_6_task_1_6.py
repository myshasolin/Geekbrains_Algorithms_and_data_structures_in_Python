# функция, формирующая в генераторе и возвращающая строку от a до b
# Второй вариант решения. этот способ в разы быстрее рекурсивной функции + не имеет ограничений стека памяти в 1000.
# Последовательность от 1 до 10 млн. сформировалась в миг

# вес больше предыдущей версии раз так в 10, так как в такой простой программе есть генератор

from sum_size import sum_size, operating_system_version


operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def my_func(a, b):
    if a < b:
        my_list = [i for i in range(a, b + 1)]
        print(str(my_list)[1:-1])
    elif a > b:
        my_list = [i for i in range(a, b - 1, -1)]
        print(str(my_list)[1:-1])
    sum_size(a, b, my_list)


my_func(50, 0)

# использовано переменных: 3
# общий их вес: 524
