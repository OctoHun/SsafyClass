def mergeSort(list, p, q):
    if p >= q:
        return
    mid = (p+q)//2
    mergeSort(list, p, mid)
    mergeSort(list, mid+1, q)
    merge(list, p, mid+1, q)


def merge(list, left, right, end):
    l, r = left, right
    mergedx = []
    mergedy = []
    while l<right and r<=end:
        if list[l] < list[r]:
            mergedx.append(list[l])
            mergedy.append(y[l])
            l += 1
        elif list[l] == list[r]:
            if y[l] < y[r]:
                mergedx.append(list[l])
                mergedy.append(y[l])
                l += 1
            else:
                mergedx.append(list[r])
                mergedy.append(y[r])
                r += 1
        else:
            mergedx.append(list[r])
            mergedy.append(y[r])
            r += 1
    while l<right:
        mergedx.append(list[l])
        mergedy.append(y[l])
        l += 1
    while r <= end:
        mergedx.append(list[r])
        mergedy.append(y[r])
        r += 1
    l = left
    for i in mergedx:
        list[l] = i
        l += 1
    l = left
    for i in mergedy:
        y[l] = i
        l += 1


n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
mergeSort(x, 0, n-1)
for i in range(n):
    print(x[i], y[i])