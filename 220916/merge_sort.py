def mergeSort(list):
    size = len(list)
    if size <= 1: # 리스트 길이가 1개라면 그 값 그대로 리턴해준다.
        return list

    mid = size//2
    left = mergeSort(list[:mid]) # 중간 전까지 왼쪽
    right = mergeSort(list[mid:]) # 중간부터 끝까지 오른쪽
    merged = merge(left, right) # 왼쪽과 오른쪽 정렬해서 합침
    return merged

def merge(list1, list2):
    merged = []
    # 한쪽이라도 리스트에 값이 있는 동안(한쪽이라도 리스트가 빌 때 까지)
    while len(list1)>0 and len(list2)>0:
        if list1[0] <= list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))

    if len(list1) > 0:
        merged += list1
    elif len(list2) > 0:
        merged += list2
    return merged


# 정렬되지 않은 리스트
list = [1, 5, 20, 49, 136, 479 ,4, 2 ,7, 10, 11]
print(mergeSort(list))

# 이대로라면 메모리를 불필요하게 사용하게 됨
# mergeSort에서 원래의 리스트를 반으로 나누었기 때문
# 처음 리스트가 100만개의 원소를 가졌다면, 50만개의 원소를 가진 리스트 2개, 다시 25만개원소의 리스트 4개....
# 이 리스트들은 함수가 종료되어야 사라지는데 재귀함수로 계속 쌓이므로 그대로 존재
# 따라서 임시배열을 사용하지 않고 코드 작성