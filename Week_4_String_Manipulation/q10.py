def binary_search_iterative(arr, target):
    s = 0
    e = len(arr) - 1

    while s <= e:
        m = s + (e - s) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            s = m + 1
        else:
            e = m - 1
            
    return -1

def binary_search_recursive(arr, target, s, e):
    if s > e:
        return -1

    m = s + (e - s) // 2

    if arr[m] == target:
        return m
    elif arr[m] < target:
        return binary_search_recursive(arr, target, m + 1, e)
    else:
        return binary_search_recursive(arr, target, s, m - 1)