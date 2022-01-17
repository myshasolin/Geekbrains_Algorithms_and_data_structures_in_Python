# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в
# несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
# функций для перевода из одной системы счисления в другую в данной задаче под запретом. Вспомните начальную школу и
# попробуйте написать сложение и умножение в столбик.

from collections import deque, OrderedDict


def dict_16():
    num_dict = OrderedDict({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '0': 0, '1': 1, '2': 2, '3': 3,
                            '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9})
    return num_dict


def normalization_of_numbers(sum_list):
    digits = deque([i for i in sum_list if i > 15])
    while digits:
        if sum_list[0] > 15:
            sum_list.insert(0, 0)
        for i in sum_list:
            if i > 15:
                dec, digit = i // 16, i % 16
                cur_pos = sum_list.index(i)
                prev_pos = cur_pos - 1
                sum_list.pop(cur_pos)
                sum_list.insert(cur_pos, digit)
                spam = sum_list.pop(prev_pos)
                sum_list.insert(prev_pos, spam + dec)
            digits = [i for i in sum_list if i > 15]
    return sum_list


def multiplying_columns(hex1, hex2):
    num1, num2, num_list, sum_list = hex_to_int(hex1), hex_to_int(hex2), [], []

    for j in num2:
        list_j = []
        for i in num1:
            local_comp = i * j
            list_j.append(local_comp)
        num_list.append(list_j)
    for i, item in enumerate(num_list):
        for j in range(i):
            item.insert(0, 0)
    for i, item in enumerate(num_list):
        for j in range(len(num2) - i - 1):
            item.append(0)
    for j in range(len(num_list[0])):
        sum_i = 0
        for i in range(len(num_list)):
            sum_i += num_list[i][j]
        sum_list.append(sum_i)
    normalization_of_numbers(sum_list)
    return sum_list


def adding_columns(hex1, hex2):
    num1, num2, list_sum = hex_to_int(hex1), hex_to_int(hex2), []
    difference = abs(len(num1) - len(num2))
    if difference:
        if len(num1) < len(num2):
            for i in range(difference):
                num1.insert(0, 0)
        else:
            for i in range(difference):
                num2.insert(0, 0)
    for i in range(len(num1)):
        num_sum = num1[i] + num2[i]
        list_sum.append(num_sum)
    normalization_of_numbers(list_sum)
    return list_sum


def hex_to_int(hex_list):
    num_list = []
    for i in hex_list:
        num_list.append(dict_16()[i])
    return num_list


def int_to_hex(num_list):
    hex_list = []
    for i in num_list:
        def dict_search(num):
            for k, v in dict_16().items():
                if v == num:
                    return k
        j = dict_search(i)
        hex_list.append(j)
    result_str = ''
    for i in hex_list:
        result_str += f'{i}'
    return result_str


num_1 = input('Пиши первое число: ').upper()
num_1_in_func = list(num_1)
num_2 = input('И второе пиши тоже: ').upper()
num_2_in_func = list(num_2)

print(f'\n{num_1} + {num_2} это у нас: {int_to_hex(adding_columns(num_1, num_2))}')
print(f'а {num_1} * {num_2} равно: {int_to_hex(multiplying_columns(num_1, num_2))}')
