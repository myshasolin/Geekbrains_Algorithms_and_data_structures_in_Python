# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.

# решение одной строкой - это если мы просто хотим получить количество подстрок без перечисления хэш и подстроек
# формируем сразу множество из хэшей, а т.к. это множество, то дубли сами удалятся. Плюс - 1 для вычитания самой строки
import hashlib


def number_of_substrings(s):
    return f"количество уникальных подстрок: " \
           f"{len({hashlib.sha1(s[i: j].encode('utf-8')).hexdigest() for i in range(len(s)) for j in range(i + 1, len(s) + 1)}) - 1}"


print(number_of_substrings(input('сюда строку: ')))
