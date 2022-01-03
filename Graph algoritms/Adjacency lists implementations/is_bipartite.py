# Sprawdzenie czy graf jest dwudzielny

from collections import deque


def bfs_list(G, s):
    n = len(G)
    color = [None for _ in range(n)]
    current_color = True

    Q = deque()
    color[s] = False
    Q.appendleft(s)

    while Q:
        v = Q.pop()
        for u in G[v]:
            if color[u] == color[v]:
                return False
            elif color[u] is None:
                color[u] = current_color
                Q.appendleft(u)

        current_color = not current_color

    return True


def is_bipartite_list(G):
    return bfs_list(G, 0)


if __name__ == '__main__':
    L1 = [[1, 2],
          [0, 2],
          [0, 1]]

    L2 = [[1, 3],
          [0, 2],
          [1, 3],
          [0, 2]]

    L3 = [[1, 2],
          [3],
          [1, 5],
          [4],
          [5],
          [6],
          []]

    print('list:')
    print(is_bipartite_list(L1))
    print(is_bipartite_list(L2))
    print(is_bipartite_list(L3))
    print()