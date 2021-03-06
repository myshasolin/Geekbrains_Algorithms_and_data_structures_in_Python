# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

x1 = float(input('пиши координаты X для первой точки: '))
y1 = float(input('пиши координаты Y для первой точки: '))
x2 = float(input('пиши координаты X для второй точки: '))
y2 = float(input('пиши координаты Y для второй точки: '))

if x1 == x2:
    print(f'x = {x1:.2f}')
else:
    k = (y2 - y1)/(x2 - x1)
    b = y1 - k * x1
    if b > 0:
        print(f'А вот и уравнение прямой:\ny = {round(k, 2)}x + {round(b, 2)}')
    else:
        print(f'А вот и уравнение прямой:\ny = {round(k, 2)}x - {round(abs(b), 2)}')
