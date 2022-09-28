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
        if arr[l][0] < arr[r][0]:
            merged.append(arr[r])
            r += 1
        else:
            merged.append(arr[l])
            l += 1
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
arr = [list(map(int, input().split())) for _ in range(n)]
grade = [0] * n
for i in range(n):
    temp = 1
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            temp += 1
    print(temp, end = ' ')