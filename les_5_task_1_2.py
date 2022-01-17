# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import ChainMap

number = int(input('Пиши конторки свои: '))
prod_list, q1, q2, q3, q4, year_profits = [], [], [], [], [], []

for i in range(1, number + 1):
    prod_list.append(input(f'Название компании нумбер {i} пиши: '))
    q1.append(int(input(f'Доход за 1 квартал: ')))
    q2.append(int(input(f'Доход за 2 квартал: ')))
    q3.append(int(input(f'Доход за 3 квартал: ')))
    q4.append(int(input(f'Доход за 4 квартал: ')))

prod_map = ChainMap()
for i in range(number):
    prod_map = prod_map.new_child({'name': prod_list[i], 'q1': q1[i], 'q2': q2[i], 'q3': q3[i], 'q4': q4[i]})
print(prod_map)

for i in range(number):
    year_profit = q1[i] + q2[i] + q3[i] + q4[i]
    year_profits.append(year_profit)
print(f'Годовые доходы {number} предприятий: {year_profits}')


def list_sum(res_list):
    res_sum = 0
    for x in res_list:
        res_sum += x
    return res_sum


avg_sum_year = (list_sum(q1) + list_sum(q2) + list_sum(q3) + list_sum(q4)) / number

print(f'Средний доход за год: {avg_sum_year}')

not_completed, completed = [], []

for i in range(len(year_profits)):
    if year_profits[i] > avg_sum_year:
        not_completed.append(prod_list[i])
    else:
        completed.append(prod_list[i])

print(f'Прибыль выше среднего у:\n{not_completed}\n и ниже у:\n{completed}')
