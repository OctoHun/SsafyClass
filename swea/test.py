def mergeSort(start, end):
    if start >= end:
        return
    mid = (start+end)//2
    mergeSort(start, mid)
    mergeSort(mid+1, end)
    merge(start, mid+1, end)


def merge(left, right, end):
    merged = []
    l, r = left, right
    while l < right and r <= end:
        if arr[l] < arr[r]:
            merged.append(arr[l])
            l += 1
        else:
            merged.append(arr[r])
            r += 1
    while l < right:
        merged.append(arr[l])
        l += 1
    while r <= end:
        merged.append(arr[r])
        r += 1
    l = left
    for i in merged:
        arr[l] = i
        l += 1


arr = [1, 5, 2, 6, 7, 4, 5, 8, 0, 6]
mergeSort(0, len(arr)-1)
print(arr)
