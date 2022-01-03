# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму вве-
# денных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

while True:
    try:
        matrix = [[int(input(f'пиши {i + 1} цифру строки и дави Enter: ')) for i in range(4)] for _ in range(4)]
        break
    except ValueError:
        print('цифру надо было писать! Цифру! Давай заново\n')

for x in matrix:
    sum_line = 0
    for y in x:
        sum_line += y
        print(f'{y:<4}', end='')
    print(f'{sum_line:<4}')
