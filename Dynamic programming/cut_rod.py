def cut_rod_bottom_up(costs, n):
    incomes = [0]*(n+1)
    incomes[0] = 0
    for i in range(1, n+1):
        result = -1
        for j in range(1, i+1):
            result = max(result, costs[j] + incomes[i - j])
        incomes[i] = result
    return incomes[n]


tab = [0, 1, 5, 8, 9, 10, 17, 17, 20]
length = 5
print(cut_rod_bottom_up(tab, length))
