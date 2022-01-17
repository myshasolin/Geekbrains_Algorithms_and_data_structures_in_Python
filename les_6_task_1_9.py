# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в
# несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
# функций для перевода из одной системы счисления в другую в данной задаче под запретом. Вспомните начальную школу и
# попробуйте написать сложение и умножение в столбик.

# этот вариант очень тяжелый, хоть в нём и на 10 переменных меньше, чем в варианта les_6_task_1_8, но много очередей
# (deque), вразнос проигрывает двум предыдущим. Сумма внизу

from collections import deque
from sum_size import sum_size, operating_system_version


operating_system_version()
# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def func_sum(num1, num2):
    my_num, result, mov = my_dict(), deque(), 0
    num1, num2 = deque(num1), deque(num2)
    if len(num2) > len(num1):
        num1, num2 = deque(num2), deque(num1)

    while num1:
        if num2:
            eggs = my_num[num1.pop()] + my_num[num2.pop()] + mov
        else:
            eggs = my_num[num1.pop()] + mov
        mov = 0
        if eggs < 16:
            result.appendleft(my_num[eggs])
        else:
            result.appendleft(my_num[eggs - 16])
            mov = 1
    if mov:
        result.appendleft('1')
    # sum_size(my_num, result, mov, num1, num2, eggs) => 3100
    return the_end_result(result)


def func_mult(num1, num2):
    my_num, result = my_dict(), deque()
    spam = deque([deque() for i in range(len(num2))])
    num1, num2 = num1.copy(), deque(num2)
    for i in range(len(num2)):
        m = my_num[num2.pop()]
        for j in range(len(num1) - 1, -1, -1):
            spam[i].appendleft(m * my_num[num1[j]])
        for _ in range(i):
            spam[i].append(0)
    transfer = 0
    for x in range(len(spam[-1])):
        res = transfer
        for y in range(len(spam)):
            if spam[y]:
                res += spam[y].pop()
        if res < 16:
            result.appendleft(my_num[res])
        else:
            result.appendleft(my_num[res % 16])
            transfer = res // 16
    if transfer:
        result.appendleft(my_num[transfer])
        # sum_size(my_num, result, spam, num1, num2, i, m, j, transfer, x, y) => 3264
    return the_end_result(result)


def my_dict():
    my_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
              'D': 13, 'E': 14, 'F': 15, 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
              10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    # sum_size(my_num) => 1176
    return my_num


def the_end_result(result):
    result_str = ''
    for i in result:
        result_str += f'{i}'
    # sum_size(result_str, i) => 101
    return result_str


num_1 = input('Пиши первое число: ').upper()
num_in_func_1 = list(num_1)
num_2 = input('И второе число пиши тоже: : ').upper()
num_in_func_2 = list(num_2)

print(f'сложили: \n{num_1} + {num_2} = {func_sum(num_in_func_1, num_in_func_2)}')
print(f'умножили: \n{num_1} * {num_2} = {func_mult(num_in_func_1, num_in_func_2)}')

# sum_size(num_1, num_2, num_in_func_1, num_in_func_2) => 228
# sum_size(func_sum, func_mult, my_dict, the_end_result) => 544

# использовано переменных: 28
# общий их вес: 8413
