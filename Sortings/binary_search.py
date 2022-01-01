def bin_search(arr, x):
    p = 0
    r = len(arr) - 1
    while r >= p:
        mid = (p+r)//2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            r = mid - 1
        else:
            p = mid + 1
    return False