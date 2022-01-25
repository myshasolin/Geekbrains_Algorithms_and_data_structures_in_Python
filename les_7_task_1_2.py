# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
# сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

# второй вариант - покучерявей первого, но с той же скоростью по результатом - от O(n) до 0(n**2). Его суть - во
# внутренней функции мы бегаем по нашему неотсортированному списку и складываем во временный список "0", если первый
# элемент больше второго, и "1" если первый элемент меньше второго. Рано или поздно временный список будет состоять
# только из нулей. Когда такое произойдёт, мы вернём в цикл основной функции False и это позволит нам "досрочо" выйти
# из цикла while, т.к. все элементы уже на своих местах
import random

my_list = [random.randint(-100, 100) for i in range(20)]


def bubble_sort_2(array):
    def testing(array_for_testing):
        spam = []
        for x in range(len(array_for_testing) - 1):
            spam.append(0) if array_for_testing[x] >= array_for_testing[x + 1] else spam.append(1)
        if spam.count(1):
            return True
        else:
            return False
    n = 1
    while n < len(array) and testing(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return n - 1


print(f'Было:\n{my_list}\nА вот что у нас получилось:\nКоличество итераций: {bubble_sort_2(my_list)}\n{my_list}')