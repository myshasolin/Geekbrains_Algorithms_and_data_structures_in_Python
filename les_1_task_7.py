# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('пиши год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('это был високосный год, несчастливый год')
else:
    print('год как год, обычный год')
