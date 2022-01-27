# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые
# необходимо обойти
from collections import deque

g = [[0, 0, 1, 1, 9, 0, 0, 0],
     [0, 0, 9, 4, 0, 0, 5, 0],
     [0, 9, 0, 0, 3, 0, 6, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 5, 0],
     [0, 0, 7, 0, 8, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 2, 0]]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float("inf")] * length
    parent = [-1] * length
    path = [None] * length
    path_start = start
    cost[start] = 0
    min_cost = 0
    while min_cost < float("inf"):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        min_cost = float("inf")
        for x in range(length):
            if min_cost > cost[x] and not is_visited[x]:
                min_cost = cost[x]
                start = x
    for y in range(length):
        if y != path_start:
            node = y
            if parent[node] == -1:
                path[y] = deque([f'Нет пути от вершины {s} до вершины {node}'])
            else:
                path[y] = deque([node])
                while True:
                    path[y].appendleft(parent[node])
                    if parent[node] == path_start:
                        break
                    node = parent[node]
    return cost, path


s = int(input("От какой вершины считать? "))
cost, path = dijkstra(g, s)

for i in range(len(g)):
    if i != s:
        print(f"Путь от {s} до вершины {i}: {list(path[i])}, стоимость: {cost[i]}")
