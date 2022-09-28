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


def find(a, p, q, target):
    global ans
    if p >= q:
        if a == arr[target]:
            ans = 1
        return
    if a == arr[target]:
        ans = 1
        return
    elif a > arr[target]:
        find(a, target+1, q, (target+1+q)//2)
    else:
        find(a, p, target, (p+target)//2)



n = int(input())
arr = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))
mergeSort(arr, 0, n-1)
for i in range(m):
    ans = 0
    find(num[i], 0, n-1, (n-1)//2)
    if ans:
        print(1)
    else:
        print(0)