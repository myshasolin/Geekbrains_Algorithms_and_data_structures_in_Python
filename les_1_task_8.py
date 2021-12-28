# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num_1 = int(input('первое число: '))
num_2 = int(input('второе число: '))
num_3 = int(input('ну и третье: '))

if num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
    print(f'вот оно, среднее: {num_1}')
elif num_1 < num_2 < num_3 or num_3 < num_2 < num_1:
    print(f'вот оно, среднее: {num_2}')
else:
    print(f'вот оно, среднее: {num_3}')
