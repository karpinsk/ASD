def counting_sort(arr, k):
    n = len(arr)
    result_arr = [0] * n
    count_arr = [0] * k
    for i in range(n):
        count_arr[arr[i]] += 1          # counting how many unique numbers are there in an array
    for i in range(1, k):
        count_arr[i] += count_arr[i-1]      # how many elements are less or equal than i
    for i in range(n-1, -1, -1):
        count_arr[arr[i]] -= 1
        result_arr[count_arr[arr[i]]] = arr[i]
    for i in range(n):
        arr[i] = result_arr[i]              # copy to source array


tab = [17, 33, 2, 0, 42, 2, 777, 322, 5, 15]
k = max(tab)+1
counting_sort(tab, k)
print(tab)