from collections import deque


def topological_sort_matrix(G):
    n = len(G)
    visited = [False for _ in range(n)]
    result = deque()

    def dfs_visit(v):
        visited[v] = True

        for u in range(n):
            if G[v][u] == 1 and not visited[u]:
                dfs_visit(u)

        result.appendleft(v)

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    return list(result)
