def merge(list, left, right, end):
    merged = []
    l, r = left, right
    while l < right and r <= end:
        if list[l] < list[r]:
            merged.append(list[l])
            l += 1
        else:
            merged.append(list[r])
            r += 1
    while l < right:
        merged.append(list[l])
        l += 1
    while r <= end:
        merged.append(list[r])
        r += 1
    l = left
    for n in merged:
        list[l] = n
        l += 1


def mergeSort(list, p, q):
    if p >= q:
        return
    mid = (p+q) // 2
    mergeSort(list, p, mid)
    mergeSort(list, mid+1, q)
    merge(list, p, mid+1, q)


t = int(input())
for tc in range(1, t+1):
    p = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in arr:
        cnt += 1
    length = cnt
    mergeSort(arr, 0, length-1)
    print('#%d' %tc, arr[0]*arr[length-1])