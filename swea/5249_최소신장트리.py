def mergeSort(p, q):
    if p >= q:
        return
    mid = (p+q)//2
    mergeSort(p, mid)
    mergeSort(mid+1, q)
    merge(p, mid+1, q)


def merge(left, right, end):
    l, r = left, right
    merged = []
    while l < right and r <= end:
        if arr[l][2] < arr[r][2]:
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


def findset(x):
    while x != tree[x]:
        x = tree[x]
    return x


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(e)]
    mergeSort(0, e - 1)
    tree = [0] * (v+1)
    for i in range(v+1):
        tree[i] = i
    cnt = 0
    ans = 0
    for i in range(e):
        if findset(arr[i][0]) != findset(arr[i][1]):
            tree[findset(arr[i][1])] = findset(arr[i][0])
            ans += arr[i][2]
            cnt += 1
        if cnt == v:
            break
    print('#%d' %tc, ans)