# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

counter_of_even_numbers, counter_of_odd_numbers = 0, 0
a_string_of_even_numbers, a_string_of_odd_numbers = '', ''
custom_digit = int(input('пиши число: '))

while custom_digit > 0:
    if custom_digit % 2 == 0:
        counter_of_even_numbers += 1
        a_string_of_even_numbers += f'{str(custom_digit)[-1]}'
    else:
        counter_of_odd_numbers += 1
        a_string_of_odd_numbers += f'{str(custom_digit)[-1]}'
    custom_digit //= 10

print(f'четных: {counter_of_even_numbers} и они такие: {a_string_of_even_numbers[::-1]}\nа нечётных: '
      f'{counter_of_odd_numbers} ну и вот они, красивые наши: {a_string_of_odd_numbers[::-1]}')
