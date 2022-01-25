# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

# решение рекурсией с генератором, собирающим в себя левую и правую часть. Мы сортируем список, а потом просто берём
# себе средний элемент - это медиана и есть

from random import randint
from statistics import median

my_list = [randint(1, 100) for i in range(21)]


def med(lst):
    def quicksort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            min_el = [i for i in array[1:] if i <= pivot]
            max_el = [i for i in array[1:] if i > pivot]
            return quicksort(min_el) + [pivot] + quicksort(max_el)
    srt = quicksort(lst)
    md = srt[(len(srt) // 2)]
    return md


sort = med(my_list)
print(f'список:\n{my_list}\nа вот и медиана наша:\n{sort}')
# print(f'проверка функцией median(): {median(my_list)}')
