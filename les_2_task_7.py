# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

number = int(input('пиши давай своё любое натуральное число: '))
left_part = 0
for i in range(1, number + 1):
    left_part += i
right_part = number * (number + 1) // 2
print(f'левая часть:  {left_part}\nправая часть: {right_part}\nчтд')