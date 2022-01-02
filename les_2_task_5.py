# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

num = 0
for i in range(32, 128):
    num += 1
    if num == 10:
        separator = '\n'
        num -= 10
    else:
        separator = ''
    if i < 100:
        print(f'{i}  это - {chr(i)}   ', end=separator)
    else:
        print(f'{i} это - {chr(i)}   ', end=separator)
