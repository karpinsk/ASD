def updown(arr):
    n = len(arr)
    up = [1] * n  # rosnący
    down = [1] * n  # malejący

    for i in range(2, n):
        for j in range(i):
            if arr[i] > arr[j]:
                up[i] = max(up[i], 1 + up[j])

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                down[i] = max(down[i], 1 + down[j])

    longest = float("-inf")

    for i in range(n):
        longest = max(longest, up[i] + down[i] - 1)

    return longest


tab = [4, 2, 5, 7, 6, 9, 1]
print(updown(tab))
