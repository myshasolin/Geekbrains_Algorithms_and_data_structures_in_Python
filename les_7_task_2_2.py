# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# второй способ алгоритма слияния, с использованием модуля operator
import operator
import random

my_list = [random.randint(0, 49) for i in range(20)]
print(f'Было:\n{my_list}')


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)

        def merge(left, right, compare):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if compare(left[i], right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            return result

        return merge(left, right, compare)


sort = merge_sort(my_list)
print(f'а вот что у нас получилось:\n{sort}')
