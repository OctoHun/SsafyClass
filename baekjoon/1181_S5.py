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
        if len(arr[l]) > len(arr[r]):
            merged.append(arr[r])
            r += 1
        elif len(arr[l]) == len(arr[r]):
            if arr[l] > arr[r]:
                merged.append(arr[r])
                r += 1
            else:
                merged.append(arr[l])
                l += 1
        else:
            merged.append(arr[l])
            l += 1
    while l < right:
        merged.append(arr[l])
        l += 1
    while r<=end:
        merged.append(arr[r])
        r += 1
    l = left
    for i in merged:
        arr[l] = i
        l += 1


n = int(input())
arr = [input() for _ in range(n)]
arr = set(arr)
arr = list(arr)
length = len(arr)
mergeSort(arr, 0, length-1)
for i in range(length):
    print(arr[i])