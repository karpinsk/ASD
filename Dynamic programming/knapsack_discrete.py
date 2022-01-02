# f(i,c) - największy zysk, który możemy uzyskać, rozważająć pierwsze i przedmiotów, nie przekraczając pojemności c
# ----------------------------------------
# Zależność rekurencyjna:
# f(0, c) = P[0], jeżeli waga zerowego przedmiotu jest mniejsza od pojemności plecaka
# f(0, c) = 0, jeżeli waga zerowego przedmiotu przekracza pojemność plecaka
# f(i, 0) = 0 - zakładamy, że nie istnieją przedmioty o wadze 0
# f(i, c) = max{ f(i-1,c), f(i-1, c-W[i]) + P[i]} - albo nie bierzemy ten przedmiot i rozważamy przedmioty 0...i-1,
#                                                   albo bierzemy ten przedmiot, zmniejszając pojemność plecaka,
#                                                   i zwiększając łączny zysk

def knapsack_discrete(weights, profits, capacity):
    n = len(weights)
    f = [[0]*(capacity+1) for i in range (n)]
    for w in range(weights[0], capacity + 1):   # wykorzystujemy zerowy przedmiot
        f[0][w] = profits[0]
    for i in range(1, n):                   # sprawdzamy kolejny przedmiot
        for w in range(1, capacity+1):
            f[i][w] = f[i-1][w]             # zawsze możemy nie wziąć i-tego przedmiotu
            if w >= weights[i]:               # jak tylko da się włożyć i-ty przedmiot do plecaka
                f[i][w] = max(f[i][w], f[i-1][w - weights[i]] + profits[i])     # maks. z dwóch opcji: brać albo nie
    return f

def get_solution(f, weights, profits, i, w):      # zwraca listę wybranych przedmiotów
    if i == 0:
        if w >= weights[0]:
            return [0]
        return []
    if w >= weights[i] and f[i][w] == f[i - 1][w - weights[i]] + profits[i]:        # jeśli możemy dołożyć i-ty przedmiot
        return get_solution(f, weights, profits, i - 1, w - weights[i]) + [i]
    return get_solution(f, weights, profits, i - 1, w)


W = [5, 7, 1, 11, 2, 15]
P = [7, 10, 3, 8, 4, 20]
C = 18

res = knapsack_discrete(W, P, C)
print(res[len(W)-1][C])
print(get_solution(res, W, P, len(W)-1, C))

