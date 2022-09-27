def mergeSort(arr, p, q):
    if p >= q-1:
        return
    mid = (p+q)//2
    mergeSort(arr, p, mid)
    mergeSort(arr, mid, q)
    merge(arr, p, mid, q)


def merge(arr, left, right, end):
    global cnt
    l, r = left, right
    merged = []
    if arr[right-1] > arr[end-1]:
        cnt += 1
    while l < right and r < end:
        if arr[l] < arr[r]:
            merged.append(arr[l])
            l += 1
        else:
            merged.append(arr[r])
            r += 1
    while l < right:
        merged.append(arr[l])
        l += 1
    while r < end:
        merged.append(arr[r])
        r += 1
    l = left
    for i in merged:
        arr[l] = i
        l += 1


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    mergeSort(arr, 0, len(arr))
    print('#%d' %tc, arr[n//2], cnt)
