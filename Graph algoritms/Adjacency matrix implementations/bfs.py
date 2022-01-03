# BFS na macierzy sąsiedztwa. Najkrótsze ścieżki w grafie nieważonym

from queue import PriorityQueue


def BFS(G, s):
    V = len(G)
    Q = PriorityQueue()
    result = [(0, 0)] * V  # tablica wynikowa (parent i,di)

    visited = [False] * V  # tworzymy tablicę odwiedzonych wierzchołków i ustawiamy ich wartości na false

    result[s] = (None, 0)  # deklarujemy wartości dla wywoływanego wierzchołka
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in range(V):
            if G[u][v] == 1:
                if not visited[v]:
                    visited[v] = True
                    result[v] = (u, result[u][1] + 1)
                    Q.put(v)
    return result


G = [[0, 1, 1, 1, 0],
     [1, 0, 0, 1, 1],
     [1, 0, 0, 1, 1],
     [1, 1, 1, 0, 1],
     [0, 1, 1, 1, 0]]

print(BFS(G, 0))