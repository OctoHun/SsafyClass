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


def search(target, l, r, flag):
    global cnt
    m = (l+r)//2
    if arrn[m] == target:
        if flag != 0:
            cnt += 1
        return
    if l >= r:
        return
    elif arrn[m] > target:
        if flag == 1:
            return
        elif flag == -1:
            search(target, l, m-1, 1)
    else:
        if flag == 1:
            search(target, m+1, r, -1)
        elif flag == -1:
            return



t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arrn = list(map(int, input().split()))
    arrm = list(map(int, input().split()))
    mergeSort(arrn, 0, n-1)
    cnt = 0
    for i in range(m):
        if arrn[(n-1)//2] == arrm[i]:
            cnt += 1
        elif arrn[(n-1)//2] < arrm[i]:
            search(arrm[i], (n-1)//2+1, n-1, -1)
        else:
            search(arrm[i], 0, (n-1)//2-1, 1)
    print('#%d' %tc, cnt)
