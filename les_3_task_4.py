# Определить, какое число в массиве встречается чаще всего.
from random import randint

my_list = [randint(1, 8) for i in range(20)]
print(f'список:\n{my_list}')

result = number = 0
for i in my_list[:]:
    if my_list.count(i) > result:
        result = my_list.count(i)
        number = i

print(f'число {number} встречается {result} раз')
