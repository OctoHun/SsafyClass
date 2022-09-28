def mergeSort(arr, p, q):
    if p >= q:
        return
    mid = (p+q)//2
    mergeSort(arr, p, mid)
    mergeSort(arr, mid+1, q)
    merge(arr, p, mid+1, q)


def merge(arr, left, right, end):
    l, r = left, right
    merged = []
    while l < right and r <= end:
        if int(arr[l][0]) <= int(arr[r][0]):
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
arr = list(input().split() for _ in range(n))
mergeSort(arr, 0, n-1)
for i in range(n):
    print(arr[i][0], arr[i][1])