# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся
# пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
# неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    number_1 = int(input('пиши число 1: '))
    number_2 = int(input('пиши число 2: '))
    choosing_an_answer = input('пиши "+", "-", "*", "/", для выхода пиши "0": ')
    if choosing_an_answer == '+':
        print(f'сложижи {number_1} и {number_2} и получили: {number_1 + number_2}')
    elif choosing_an_answer == '-':
        print(f'{number_1} - {number_2} это у нас: {number_1 - number_2}')
    elif choosing_an_answer == '*':
        print(f'умножим {number_1} на {number_2} и вот что выйдет: {number_1 * number_2}')
    elif choosing_an_answer == '/':
        if number_2 == 0:
            print('на 0 делить нельзя, это ж всем известная тема, не тупи')
        else:
            print(f'{number_1} разделить на {number_2} это у нас: {number_1 / number_2}')
    elif choosing_an_answer == '0':
        print('до новых встреч)')
        break
    else:
        print('введена какая-то шляпа, попробуй ещё раз')
