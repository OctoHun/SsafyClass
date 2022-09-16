# 원래의 merge_sort는 메모리를 불필요하게 사용하게 됨
# mergeSort에서 원래의 리스트를 반으로 나누었기 때문
# 처음 리스트가 100만개의 원소를 가졌다면, 50만개의 원소를 가진 리스트 2개, 다시 25만개원소의 리스트 4개....
# 이 리스트들은 함수가 종료되어야 사라지는데 재귀함수로 계속 쌓이므로 그대로 존재
# 따라서 임시배열을 사용하지 않고 코드 작성

def mergeSort(list, p, q): # 이제 전체 리스트와 배열의 왼쪽 인덱스, 오른쪽 인덱스를 전달
    if p >= q: # p와 q가 교차하면 끝
        return
    mid  = (p + q) // 2
    mergeSort(list, p, mid)
    mergeSort(list, mid+1, q)
    merge(list, p, mid+1, q)

def merge(list, left, right, end):
    merged = []
    l, r = left, right
    while l < right and r <= end:
        if list[l] <= list[r]:
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


list = [1, 5, 20, 49, 136, 479 ,4, 2 ,7, 10, 11]
sorted = mergeSort(list, 0, len(list)-1)
print(list)