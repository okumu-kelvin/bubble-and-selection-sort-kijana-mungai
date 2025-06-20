def selection_sort(arr):
    # TODO: Implement selection sort
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


data = [14, 12, 11, 67, 98]
sorted_data = selection_sort(data)
print(sorted_data)


