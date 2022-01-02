def diff(a, b):      # porównanie dwóch symboli
    if a == b:
        return 0
    return 1

def Levenstein(str1,str2):
    n = len(str1)+1
    m = len(str2)+1
    D = [[None]*m for i in range(n)]
    for i in range(n):
        D[i][0] = i
    for j in range(m):
        D[0][j] = j
    for i in range(1, n):
        for j in range(1,m):     # min( add , delete , change )
            D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+diff(str1[i-1],str2[j-1]))
            res = D[n-1][m-1]
    return res


first = "Interstellar"
second = "Alterstellar"
print(Levenstein(first, second))
