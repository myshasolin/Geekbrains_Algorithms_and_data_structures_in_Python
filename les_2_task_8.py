# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

number_of_numbers = int(input('сколько будет у нас этих самых последовательностей? '))
number = input('какую цифру будем искать? ')
ready_list, result, count = '', None, 1

while number_of_numbers != 0:
    ready_list += input(f'пиши {count} список и дави Enter: ') + '\n'
    if ready_list.find(number):
        result = ready_list.count(number)
    number_of_numbers -= 1
    count += 1
print(f'вот такой список получился:\n{ready_list}а цифра {number} встречается в нём {result} раз')
