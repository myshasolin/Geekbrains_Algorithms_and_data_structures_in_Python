# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

# Нахождение медианы с помощью алгоритма "quickselect" Тони Хоара. О нём вот здесь: https://habr.com/ru/post/346930/

import random
# from statistics import median

m = 5
my_list = [random.randint(1, 50) for i in range(2 * m + 1)]
check = my_list.copy()


def quick(array):
    def _quick(_array, index):
        if len(_array) == 1:
            assert index == 0
            return _array[index]
        pivot = random.choice(_array)
        min_list, max_index, pivots = [], [], []
        for i in _array:
            if i < pivot:
                min_list.append(i)
            elif i > pivot:
                max_index.append(i)
            else:
                pivots.append(i)
        if index < len(min_list):
            return _quick(min_list, index)
        elif index < len(min_list) + len(pivots):
            return pivots[0]
        else:
            return _quick(max_index, index - len(min_list) - len(pivots))
    if len(array) % 2 == 1:
        return _quick(array, len(array) // 2)
    else:
        return 0.5 * (_quick(array, len(array) // 2 - 1) + _quick(array, len(array) // 2))


print(f'Вот массив:\n{my_list}\nа вот и медиана: {quick(my_list)}')
# print(f'проверка функцией median(): {median(check)}')
