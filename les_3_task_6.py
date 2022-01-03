# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint

my_list = [randint(0, 999) for i in range(20)]
print(f'вот наш список:\n{my_list}\n')

index_min = index_max = result = 0
value_min = value_max = my_list[0]
for x, y in enumerate(my_list[1:], 1):
    if y < value_min:
        value_min, index_min = y, x
    elif y > value_max:
        value_max, index_max = y, x

print(f'минимальное число в нём: {value_min}\nа вот и максимальное: {value_max}')

if index_min < index_max:
    print(f'{value_min} находится левее {value_max}')
    result_list = my_list[index_min + 1:index_max]
    print(f'вот что у нас между этими числами: {result_list}')
else:
    print(f'число {value_min} в списке оказалось справа от {value_max}')
    result_list = my_list[index_max + 1:index_min]
    print(f'вот что между этими нашими большими и маленькими затесалось: {result_list}')

for i in result_list:
    result += i
print(f'сумма чисел между ними вот она: {result}')
