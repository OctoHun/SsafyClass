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
        if arr[l][1] < arr[r][1]:
            merged.append(arr[l])
            l += 1
        elif arr[l][1] == arr[r][1]:
            if arr[l][0] < arr[r][0]:
                merged.append(arr[l])
                l += 1
            else:
                merged.append(arr[r])
                r += 1
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


def work():
    end = arr[0][1]
    cnt = 1
    for i in range(1, n):
        if end <= arr[i][0]:
            cnt += 1
            end = arr[i][1]
    return cnt


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mergeSort(arr, 0, n-1)
    ans = work()
    print('#%d' %tc, ans)