from collections import deque


def topological_sort_list(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    result = deque()

    def dfs_visit(v):
        visited[v] = True

        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                dfs_visit(u)

        result.appendleft(v)

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    return list(result)
