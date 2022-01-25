# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# Эта сортировка — хороший пример использования принципа «разделяй и властвуй». Сначала задача разбивается на несколько
# подзадач меньшего размера. Затем эти задачи решаются с помощью рекурсивного вызова или непосредственно  если их
# размер достаточно мал. Наконец, их решения комбинируются  и получается решение исходной задачи.
# Сложность алгоритма - n log n
# Устойчивость (стабильность) - устойчивый
# Тип (категория) - слиянием
# Потребление памяти - не требует доп.памяти

# отличное описание метода и его код здесь:
# https://pythonist.ru/sortirovka-sliyaniem-dlya-teh-kto-ne-hochet-prosto-ispolzovat-sort/

import random
my_list = [random.randint(0, 49) for i in range(20)]


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left, right = nums[:mid], nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1


print(f'Было:\n{my_list}')
merge_sort(my_list)
print(f'А вот что у нас получилось:\n{my_list}')
