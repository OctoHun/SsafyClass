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
            merged.append(arr[r])
            r += 1
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


def carry():
    i = 0
    j = 0
    result = 0
    while i<n and j<m:
        if arrm[j] >= arrn[i]:
            result += arrn[i]
            i += 1
            j += 1
        else:
            i += 1
    return result


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arrn = list(map(int, input().split()))
    arrm = list(map(int, input().split()))
    mergeSort(arrn, 0, n-1)
    mergeSort(arrm, 0, m-1)
    weight = carry()
    print('#%d' %tc, weight)