# Sprawdzenie czy graf jest dwudzielny

from collections import deque


def bfs_matrix(G, s):
    n = len(G)
    color = [None for _ in range(n)]
    current_color = True

    Q = deque()
    color[s] = False
    Q.appendleft(s)

    while Q:
        v = Q.pop()
        for u in range(n):
            if G[v][u] == 1 and color[u] == color[v]:
                return False
            elif G[v][u] == 1 and color[u] is None:
                color[u] = current_color
                Q.appendleft(u)

        current_color = not current_color

    return True


def is_bipartite_matrix(G):
    return bfs_matrix(G, 0)


if __name__ == '__main__':
    M1 = [[0, 1, 1],
          [1, 0, 1],
          [1, 1, 0]]

    M2 = [[0, 1, 0, 1],
          [1, 0, 1, 0],
          [0, 1, 0, 1],
          [1, 0, 1, 0]]

    M3 = [[0, 1, 1, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0]]

    print('matrix:')
    print(is_bipartite_matrix(M1))
    print(is_bipartite_matrix(M2))
    print(is_bipartite_matrix(M3))
    print()