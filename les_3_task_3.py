# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint


def recycling_the_list(user_list, step):
    max_num, min_num, max_index, min_index = 0, 100, 0, 0
    if step == 0:
        return ''
    for i, item in enumerate(user_list):
        if item > max_num:
            max_num, max_index = item, i
        elif item < min_num:
            min_num, min_index = item, i
    print(f'\nсписок\n{user_list}\nбольшее число: {max_num} меньшее число: {min_num}\nиндекс большего числа {max_index}'
          f' и меньшего числа {min_index}')
    user_list[max_index], user_list[min_index] = user_list[min_index], user_list[max_index]
    recycling_the_list(user_list, step-1)


recycling_the_list([randint(1, 100) for i in range(10)], 2)
