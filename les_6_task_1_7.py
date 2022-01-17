# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в
# несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
# функций для перевода из одной системы счисления в другую в данной задаче под запретом. Вспомните начальную школу и
# попробуйте написать сложение и умножение в столбик.

# мз трех вариантов рализации задачи этот самый легкий по весу и короткий по коду. Сумма внизу

from collections import defaultdict, deque
from sum_size import sum_size, operating_system_version

operating_system_version()


# win32 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]


def size_calculation():
    def trans_dex(string):
        dex, num = 0, deque(string)
        num.reverse()
        for i in range(len(num)):
            dex += table[num[i]] * 16 ** i
        # sum_size(dex, num), dex=28, num=624 => 652
        return dex

    def trans_hex(numb):
        num = deque()
        while numb > 0:
            d = numb % 16
            for i in table:
                if table[i] == d:
                    num.append(i)
            numb //= 16
        num.reverse()
        # sum_size(num, d, i, table[i]), num=624, d=28, i=50, table[i]=28 => 730
        return list(num)

    signs = '0123456789ABCDEF'
    table = defaultdict(int)
    counter = 0
    for key in signs:
        table[key] += counter
        counter += 1

    num_1 = trans_dex(input('Пиши первое число: ').upper())
    num_2 = trans_dex(input('И второе пиши тоже: ').upper())

    print(f'Сложили: {trans_hex(num_1 + num_2)}')
    print(f'Умножили: {trans_hex(num_1 * num_2)}')
    # sum_size(trans_dex, trans_hex, signs, table, counter, key, table[key], num_1, num_2) => 1147

# size_calculation()

# trans_dex(string) = 652
# trans_hex(numb) = 730
# size_calculation() = 1147

# использовано переменных: 15
# общий их вес: 2529
