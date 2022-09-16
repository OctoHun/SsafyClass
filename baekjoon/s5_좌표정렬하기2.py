def mergeSort(list, p, q): # 이제 전체 리스트와 배열의 왼쪽 인덱스, 오른쪽 인덱스를 전달
    if p >= q: # p와 q가 교차하면 끝
        return
    mid  = (p + q) // 2
    mergeSort(list, p, mid)
    mergeSort(list, mid+1, q)
    merge(list, p, mid+1, q)

def merge(list, left, right, end):
    merged = []
    merged2 = []
    l, r = left, right
    while l < right and r <= end:
        if list[l] < list[r]:
            merged.append(list[l])
            merged2.append(arr1[l])
            l += 1
        elif list[l] == list[r]:
            if arr1[l] < arr1[r]:
                merged.append(list[l])
                merged2.append(arr1[l])
                l += 1
            else:
                merged.append(list[r])
                merged2.append(arr1[r])
                r += 1
        else:
            merged.append(list[r])
            merged2.append(arr1[r])
            r += 1
    while l < right:
        merged.append(list[l])
        merged2.append(arr1[l])
        l += 1
    while r <= end:
        merged.append(list[r])
        merged2.append(arr1[r])
        r += 1

    l = left
    for n in merged:
        list[l] = n
        l += 1
    l = left
    for n in merged2:
        arr1[l] = n
        l += 1


n = int(input())
arr1 =[0] * n
arr2 = [0] * n
for i in range(n):
    arr1[i], arr2[i] = map(int, input().split())
a = mergeSort(arr2, 0, n-1)
for i in range(n):
    print(arr1[i], arr2[i])