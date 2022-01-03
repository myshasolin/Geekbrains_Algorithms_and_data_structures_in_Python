# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
from random import randint

my_list = [randint(2, 50) for i in range(10)]
print(f'итак, вот список:\n{my_list}')

my_list_copy = my_list.copy()
min_1 = my_list_copy[0]
for i in my_list_copy:
    if i < min_1:
        min_1 = i
my_list_copy.remove(min_1)
min_2 = my_list_copy[0]
for i in my_list_copy:
    if i < min_2:
        min_2 = i

print(f'вот первое минимальное: {min_1}\nа вот и второе! {min_2}')
