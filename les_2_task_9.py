# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

count = int(input('сколько чисел введём? '))
result, final_number, counter = 0, 0, 0

while count != 0:
    counter += 1
    number = int(input(f'пиши {counter} число: '))
    final_number, number_sum = number, 0
    while number != 0:
        number_sum += number % 10
        number //= 10
    if number_sum > result:
        result = number_sum
    count -= 1

print(f'у числа {final_number} наибольшая сумма цифр: {result}')
