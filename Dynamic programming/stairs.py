# Given an array of integers representing the steps of the staircase.
# At each turn, we can climb one or two steps. Find the maximum amount you can get by walking up the stairs,
# going up one or two steps each time.

def stairs(arr): # 1 2
    n = len(arr)
    first = 0
    second = arr[0]
    i = 1
    while i != n:
        tmp = second
        second = max(first + arr[i], tmp + arr[i])
        first = tmp
        i += 1
    return second


tab = [2, 1, -10, 5, -2, 1, -1, -3, 7]
print(stairs(tab))
