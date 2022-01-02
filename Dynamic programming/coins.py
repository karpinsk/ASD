# f(i) - minimalna liczba monet, potrzebna do wydania kwoty o wartości i
# ----------------------------------------
# Zależnośći rekurencyjne:
# f(-i) = 0
# f(0) = 0
# f(i) = 1 + min {f(i-coin)}, gdzie coin pewna moneta z tablicy coins

def min_coins(coins, amount):
    f = [0] * (amount+1)
    for i in range(1, amount + 1):
        if i >= coins[0]:           # nie wydamy 1 złoty jak najmniejszy nominał wynosi 3 złote
            min = f[i-coins[0]]     # python nie ma wbudowanej funkcji minimum
            for coin in coins:
                if i >= coin:       # jeśli nasza kwota jest większa od kolejnego nominału
                    curr = f[i-coin]
                    if curr < min:
                        min = curr
                else:
                    break
            f[i] = 1 + min
    return f[amount]

arr = [1, 5, 8]
print("number: ", min_coins(arr, 15))
