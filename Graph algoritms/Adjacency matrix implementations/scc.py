time = 0


def DFS(G):
    V = len(G)
    visited = [False] * V
    finish = [None] * V

    def DFSvisit(u):
        global time
        visited[u] = True

        for i in range(len(G[u])):
            v = G[u][i]
            if not visited[v]:
                visited[v] = True
                DFSvisit(v)

        # zwiękaszam czas o jedną jednostkę - to czas powrotu
        time += 1
        finish[u] = (time, u)

    for v in range(V):
        if len(G[v]) == 0:
            continue
        elif not visited[G[v][0]]:
            DFSvisit(G[v][0])

    return finish


# odwracamy krawędzi w grafie
def reverse(G):
    V = len(G)
    GG = [[] for _ in range(V)]

    # krawedz j->i zamieniamy na i->j
    for j in range(V):
        for i in (G[j]):
            GG[i].append(j)

    return GG


def components(graph):
    V = len(graph)
    # dodstajemy tablice czasow przetworzenia pierwszego DFSa - posortowane malejąco  ( krotki postaci: (czas,wierchołek) )
    times = sorted(DFS(graph))[::-1]
    print(time)

    # odwracamy krawedzi w grafie
    rev = reverse(graph)

    def visit(v):
        comp[counter].append(v)
        vis[v] = True

        for i in range(len(rev[v])):
            ngh = rev[v][i]

            if not vis[ngh]:
                vis[ngh] = True
                visit(ngh)

    vis = [False] * V

    counter = 0
    comp = []  # tablica na poszczególne spójne składowe
    for t in times:
        v = t[1]

        if not vis[v]:
            comp.append([])
            visit(v)
            counter += 1

    return comp


G = [[1, 10],
     [2],
     [0, 3],
     [4, 6],
     [5],
     [3],
     [5],
     [6, 10],
     [7],
     [5, 8],
     [9]]

print(components(G))
