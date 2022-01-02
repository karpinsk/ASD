# Zadanie: podać długośc najdłuższego podciągu, każdy element którego jest podzielny przez poprzedni element tego ciągu
# f(i) - długość najdłuższego podciądu, kończącego się na arr[i]
# ----------------------------------------
# Zależności rekurencyjne:
# f(-i) = 0
# f(0) = 1
# f(i) = max{ f(j)+1 |  j < i and arr[i] % arr[j] == 0 }
# ----------------------------------------

def lps(arr):
    n = len(arr)
    res = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] <= arr[i] and arr[i] % arr[j] == 0 and res[j] + 1 > res[i]:
                res[i] = res[j] + 1
    result = 0
    for i in range(n):
        result = max(result, res[i])
    return result


tab = [3, 6, 7, 12, 13, 120, 1]
print(lps(tab))