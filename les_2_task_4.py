# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры

the_first_element, result = 1, 0
number = int(input('пиши цифру свою: '))

for i in range(number):
    result += the_first_element
    the_first_element /= -2
print(f'а вот и сумма: {result}')
