# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import OrderedDict


def encode_string_huffman_way(string):
    """
    Функция принимает на вход строку в виде string, а возвращает (печатает) её в виде а-ля Хаффман
    """
    # разбиваем строку поэлементно
    string = [_ for _ in string]
    print(f'\nстрока поэлементно: {string}')

    # получаем словарь частот символов
    string_symbols_frequencies = {}
    for i in list(set(string)):
        string_symbols_frequencies.update({i: string.count(i)})

    # убеждаемся, что у нас в строке более чем один уникальный символ
    assert len(string_symbols_frequencies) >= 2, 'в строке не может быть только один уникальный символ!'

    # сортируем частоты символов в порядке возрастания
    string_symbols_frequencies = OrderedDict(sorted(string_symbols_frequencies.items(), key=lambda x: x[1]))
    string_symbols_frequencies = [_ for _ in string_symbols_frequencies.items()]
    print(f'\nчастоты символов в порядке возрастания: {string_symbols_frequencies}')

    # получаем дерево Хаффмана и сохраняем его обратно в переменную string_symbols_frequencies
    while True:
        if len(string_symbols_frequencies) >= 2:
            new_element = ([string_symbols_frequencies[0], string_symbols_frequencies[1]],
                           string_symbols_frequencies[0][1] + string_symbols_frequencies[1][1])
            string_symbols_frequencies = string_symbols_frequencies[2:]
            string_symbols_frequencies.append(new_element)
            string_symbols_frequencies = sorted(string_symbols_frequencies, key=lambda x: x[1])
        else:
            break
    print(f'\nдерево Хаффмана: {string_symbols_frequencies}')

    # функция для получения кодировочной таблицы из дерева Хаффмана
    def get_symbols_huffman_codes_dictionary(huffman_tree, symbols_and_their_huffman_codes={}, huffman_path=''):
        """
        Функция принимает на вход дерево Хаффмана, а возвращает кодировочную таблицу для символов строки
        Функция использует рекурсию для обхода дерева Хаффмана
        """
        # если в функцию пришло дерево с двумя листами
        if type(huffman_tree[0][0][0]) == str and type(huffman_tree[0][1][0]) == str:
            symbols_and_their_huffman_codes.update({huffman_tree[0][0][0]: f'{huffman_path}' + '0',
                                                    huffman_tree[0][1][0]: f'{huffman_path}' + '1'})
            return symbols_and_their_huffman_codes

        # если в функцию пришло дерево с листом слева и узлом справа
        elif type(huffman_tree[0][0][0]) == str:
            symbols_and_their_huffman_codes.update({huffman_tree[0][0][0]: f'{huffman_path}' + '0'})
            symbols_and_their_huffman_codes.update(
                get_symbols_huffman_codes_dictionary(huffman_tree[0][1],  # рекурсия!!!
                                                     symbols_and_their_huffman_codes,
                                                     f'{huffman_path}' + '1'))
            return symbols_and_their_huffman_codes

        # если в функцию пришло дерево с листом справа и узлом слева
        elif type(huffman_tree[0][1][0]) == str:
            symbols_and_their_huffman_codes.update({huffman_tree[0][1][0]: f'{huffman_path}' + '1'})
            symbols_and_their_huffman_codes.update(
                get_symbols_huffman_codes_dictionary(huffman_tree[0][0],  # рекурсия!!!
                                                     symbols_and_their_huffman_codes,
                                                     f'{huffman_path}' + '0'))
            return symbols_and_their_huffman_codes

        # если в функцию пришло дерево с двумя узлами
        else:
            symbols_and_their_huffman_codes.update(
                get_symbols_huffman_codes_dictionary(huffman_tree[0][0], symbols_and_their_huffman_codes,
                                                     f'{huffman_path}' + '0'))
            symbols_and_their_huffman_codes.update(
                get_symbols_huffman_codes_dictionary(huffman_tree[0][1], symbols_and_their_huffman_codes,
                                                     f'{huffman_path}' + '1'))
            return symbols_and_their_huffman_codes

    # получаем кодировочную таблицу
    symbol_codes_dictionary = get_symbols_huffman_codes_dictionary(string_symbols_frequencies[0])
    print(f'\nкодировочная таблица: {symbol_codes_dictionary}')

    # кодируем строку а-ля Хаффман
    string_encoded_huffman_way = ''
    for symbol in string:
        string_encoded_huffman_way += symbol_codes_dictionary[symbol] + ' '

    # кодируем строку в бинарный вид (для сравнения)
    string_encoded_binary = ''
    for symbol in string:
        string_encoded_binary += bin(ord(symbol))[2:] + ' '

    print(f'\nстрока в бинарном виде (для сравнения): {string_encoded_binary}')
    print(f'\nстрока а-ля Хаффман: {string_encoded_huffman_way}')


encode_string_huffman_way(input('сюда строку: '))
