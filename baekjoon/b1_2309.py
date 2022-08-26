arr = [0] * 9
for i in range(9):
    arr[i] = int(input())
for i in range(9):
    for j in range(i+1, 9):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
flag = 0
for i in range(8):
    for j in range(i+1, 9):
        cnt = 0
        for k in range(9):
            if k != i and k != j:
                cnt += arr[k]
        if cnt == 100:
            flag = 1
            break
    if flag == 1:
        break
for a in range(9):
    if a != i and a != j:
        print(arr[a])