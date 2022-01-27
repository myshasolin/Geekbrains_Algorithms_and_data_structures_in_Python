# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import randint


def generate_graph(vertices):
    """
    это у нас функция для генерации графа
    :param vertices: количество вершин
    :return: граф
    """
    gr = []
    for i in range(vertices):
        line_gr = [randint(0, vertices - 1) for _ in range(randint(0, vertices))]
        if i != vertices - 1:
            line_gr.append(i + 1)
        line_gr = list(set(line_gr))
        if line_gr.count(i):
            line_gr.remove(i)
        gr.append(line_gr)
    return gr


def vertex_search(gr, vertex, path=None):
    """
    а здесь мы ищем вершины рекурсивным алгоритмом поиска в глубину
    """
    if path is None:
        path = []
    path += [vertex]
    print(path)
    for i in gr[vertex]:
        if i not in path:
            path = vertex_search(graph, i, path)
    return path


graph = generate_graph(int(input('пиши сюда число вершин: ')))
print('вот такой вот у нас граф в виде списка смежности:')
for x, y in enumerate(graph):
    print(f'{[x]} {y}')

print()
print(f'а вот такой результ:')
vertex_search(graph, 0)
