from queue import PriorityQueue


def MST_Prim(G, s):
    V = len(G)
    Q = PriorityQueue()

    parents = [None] * V
    min_weight = [float("inf")] * V
    visited = [False] * V

    min_weight[s] = 0

    for v in range(V):
        if v != s:
            Q.put((float("inf"), v))
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True
        for v in G[u]:
            if not visited[v[1]]:
                if min_weight[v[1]] > v[0]:  # relaksacje
                    min_weight[v[1]] = v[0]
                    parents[v[1]] = u
                    Q.put(v)

    MST = []
    for i in range(V):
        if parents[i] is not None:
            MST.append((parents[i], i, min_weight[i]))
    return MST


G = [[(1, 1), (2, 5), (3, 6)],  # 0
     [(1, 0), (2, 2)],  # 1
     [(2, 1), (7, 3), (8, 6)],  # 2
     [(7, 2), (4, 4)],  # 3
     [(4, 3), (6, 5)],  # 4
     [(2, 0), (6, 4), (5, 6)],  # 5
     [(3, 0), (8, 2), (5, 5)]]  # 6

print(MST_Prim(G, 0))