import sys
from sys import getsizeof


def operating_system_version():
    print(sys.platform, sys.version)


def sum_size(*args):
    result = 0
    print('\n\n')
    for x, i in enumerate(args):
        print(f'{x+1}) переменная "{i}"\nвесит {getsizeof(i)}')
        print('_____' * 10)
        result += getsizeof(i)
    print(f'использовано переменных: {len(args)}\nобщий их вес: {result}')


# def show_size(x, level=0):
#     print('\t' * level, f'type= {x.__class__}, size = {getsizeof(x)}, object= {x}')
#
#     if hasattr(x, '__iter__'):
#         if hasattr(x, 'items'):
#             for xx in x.items():
#                 show_size(xx, level + 1)
#         elif not isinstance(x, str):
#             for xx in x:
#                 show_size(xx, level + 1)


if __name__ == '__main__':
    sum_size(5, 5, 'привет')
    ddd = [5, 6, 7]
    sum_size(ddd)




