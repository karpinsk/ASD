from collections import deque


def BFS(g, s, t, parents):
    q = deque()
    number = len(g)

    visited = [False] * number
    q.appendleft(s)
    visited[s] = True

    while len(q) != 0:
        u = q.pop()

        for i in range(number):
            if len(q) == 0: q = deque()
            if g[u][i] != 0 and visited[i] == False:
                parents[i] = u
                visited[i] = True
                q.appendleft(i)

    return visited[t]


# maksymalny przepływ z wierzchołka s do t
def Ford_Fulkerson(g, s, t):
    parents = [None] * len(g)
    flow = 0

    while BFS(g, s, t, parents):

        current = t
        cur_flow = float("inf")

        while current != s:
            if g[parents[current]][current] < cur_flow:
                cur_flow = g[parents[current]][current]
            current = parents[current]

        flow += cur_flow
        v = t

        while v != s:
            g[parents[v]][v] -= cur_flow
            g[v][parents[v]] += cur_flow
            v = parents[v]
    return flow
