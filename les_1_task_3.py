# Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

user_selection = input('Итак, что мы будем генерировать? \nпиши 1, если это случайное целое число\nпиши 2, если это '
                       'случайное вещественное число\nпиши 3, если это случайная буква\n')

if user_selection == '1':
    print('ищем случайное целое число')
    num_1 = int(input('пиши первое число диапазона: '))
    num_2 = int(input('второе число диапазона пиши тоже: '))
    print(f'а вот и наше случайное целое число: {random.randint(num_1, num_2)}')
elif user_selection == '2':
    print('ищем случайное вещественное число')
    num_1 = float(input('пиши первое число диапазона: '))
    num_2 = float(input('второе число диапазона пиши тоже: '))
    print(f'а вот и наше случайное вещественное число: {round(random.uniform(num_1, num_2), 4)}')
elif user_selection == '3':
    print('ищем случайную букву')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_1 = input('пиши первую букву: ')
    letter_2 = input('и вторую букву пиши: ')
    print(f'а вот и случайная буква из диапазона от {letter_1} до {letter_2}: '
          f'{random.choice(alphabet[alphabet.find(letter_1):alphabet.find(letter_2)+1])}')
else:
    print('введена какая-то шляпа. Программа обиделась и завершилась без результата')
