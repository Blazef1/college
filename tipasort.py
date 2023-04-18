def quick_sort_2d(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    right = []
    left = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort_2d(left) + [pivot] + quick_sort_2d(right)


array = [[441, 11, 22], [14, 1322, 44], [3, 36, 43]]


print(quick_sort_2d(array))