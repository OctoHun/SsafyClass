def selection_sort(arr): # 반목문 구현
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def selection_sort2(arr, i): # 재귀 구현
    min = i
    if i == len(arr)-1:
        return
    for j in range(i, n):
        if arr[j] < arr[min]:
            min = j
    arr[min], arr[i] = arr[i], arr[min]
    selection_sort2(arr, i+1)
