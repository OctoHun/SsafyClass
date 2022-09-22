def mergeSort(arr, p, q):
    if p >= q:
        return
    mid = (p+q)//2
    mergeSort(arr, p, mid)
    mergeSort(arr, mid+1, q)
    merge(arr, p, mid+1, q)


def merge(arr, left, right, end):
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


n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())
mergeSort(arr, 0, n-1)
for i in range(n):
    print(arr[i])