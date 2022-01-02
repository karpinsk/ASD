# f(i) - długość najdłuższego spójnego podciądu, kończącego się na arr[i]
# ----------------------------------------
# Zależności rekurencyjne:
# f(-i) = 0
# f(0) = 1
# f(i) = max{ f(j)+1 |  j < i and arr[j] < arr[i] }
# ----------------------------------------
# pred(i) - indeks elementu, który rozszerza podciąg, kończący się na indeksie i
# pred[-1] oznacza, że dany element nie rozszerza żadnego ciągu

def lis(arr):
    n = len(arr)
    f = [1] * n
    pred = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and f[j] + 1 > f[i]:
                f[i] = f[j] + 1
                pred[i] = j
    return max(f), pred

def find_max_ind(pred):     # szuka indeks elementu, który jest końcem najdłuższego spójnego podciągu
    n = len(pred)
    greatest = parents[0]
    max_ind = -1
    for i in range(n):
        if pred[i] > greatest:
            greatest = pred[i]
            max_ind = i
    return max_ind

# Możemy zastąpić funkcję find_max_ind następującym wyrażeniem: max(range(len(pred)), key = pred.__getitem__)

def print_lis(arr, pred):
    max_ind = find_max_ind(pred)
    # max_ind = max(range(len(pred)), key=pred.__getitem__)
    res = []
    while max_ind != -1:
        res.append(arr[max_ind])
        max_ind = parents[max_ind]
    for i in range(len(res) - 1, -1, -1):
        print(res[i], end=" ")

def print_lis_recursively(arr, pred, i):
    if pred[i] != -1:
        print_lis_recursively(arr, pred, pred[i])
    print(arr[i], end=" ")


tab = [5, 1, 2, 3, 6, 0, 7]
res, parents = lis(tab)
print(res)
print_lis_recursively(tab, parents, find_max_ind(parents))
print()
print_lis(tab, parents)
