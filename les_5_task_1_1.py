# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter, deque


class MyException(Exception):
    def __init__(self, message):
        self.message = message


while True:
    try:
        quantity = int(input('сюда пиши количество предприятий: '))
        sum_profit, step = Counter(), 0

        while step != quantity:
            name = input(f'пиши название компании нумбер {step+1}: ')
            profit = deque()
            for key in sum_profit.items():
                if name in sum_profit:
                    raise MyException('ошибка, аларм! Такая компания уже была в списке. Попробуем ещё раз \n')
            for y in range(4):
                profit.append(int(input(f'прибыль за {y + 1} квартал: ')))
            sum_profit[name] = profit
            step += 1

    except MyException as mess:
        print(mess)
    except ValueError:
        print('надо было цифру писать, а не лицом по клавиатуре бить. Всё заново, Карл! \n')
    else:
        break

average_profit, total_average_profit, average_profit_by_company = 0, 0, Counter()

for x, y in sum_profit.items():
    print(f'компания {x}: прибыль {sum(y)} денег, а средняя прибыль {round(sum(y) / 4, 2)} денег')
    average_profit_by_company[x] = sum(y) / 4
    average_profit += (sum(y) / 4) / quantity
    total_average_profit += sum(y) / quantity

print(f'\nсредняя прибыль для всех компаний: {round(average_profit, 2)} денег\nсредняя годовая: '
      f'{round(total_average_profit, 2)} денег\n')

did_not_fulfill_the_plan, fulfilled_the_plan, the_plan_is_equal_to_the_annual = [], [], []
for key, value in average_profit_by_company.items():
    if value > average_profit:
        fulfilled_the_plan.append(key)
    elif value == average_profit:
        the_plan_is_equal_to_the_annual.append(key)
    else:
        did_not_fulfill_the_plan.append(key)

if len(fulfilled_the_plan) == 0:
    print(f'у всех прибыль ниже среднего, как так. Вот они, наши лузеры: '
          f'\n{str(did_not_fulfill_the_plan)[1:-1]}')
elif len(did_not_fulfill_the_plan) == 0:
    print(f'у всех прибыль выше среднего, красота \n{str(fulfilled_the_plan)[1:-1]}')
else:
    print(f'прибыль больше среднего у: {str(fulfilled_the_plan)[1:-1]}\n      и меньше среднего у:'
          f' {str(did_not_fulfill_the_plan)[1:-1]}')
if not len(the_plan_is_equal_to_the_annual) == 0:
    print(f'а у этих прибыль получилась средней (как средняя за год для всех предприятий): '
          f'{str(the_plan_is_equal_to_the_annual)[1:-1]}')
