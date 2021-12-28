# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
custom_number = int(input('пиши цифру алфавита от 1 до 26: '))

if custom_number in range(1, 27):
    print(f'твоя цифра {custom_number} - это буква "{alphabet[custom_number-1]}"')
else:
    print('цифру надо было писать от 1 до 26 так-то')
