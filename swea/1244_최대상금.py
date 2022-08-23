t = int(input())
for i in range(1, t+1):
    a, n = map(str, input().split())
    n = int(n)
    length = len(a)
    arr = [0] * length
    temp = [1] * length
    for j in range(length):
        arr[j] = a[j]
    for j in range(length):
        temp[j] = arr[j]
    for j in range(length):
        for k in range(j+1, length):
            if temp[j] < temp[k]:
                temp[j], temp[k] = temp[k], temp[j]
    cnt = 0
    for j in range(n, 0, -1):
        if cnt == n:
            break
        for k in range(length):
            if cnt == n:
                break
            if arr[k] != temp[k]:
                for l in range(length-1, k, -1):
                    if arr[l] == temp[k]:
                        arr[k], arr[l] = arr[l], arr[k]
                        cnt += 1
                        break
    while cnt != n:
        if cnt + 1 < n:
            cnt += 2
        elif cnt < n:
            flag = 0
            for j in range(length-1):
                if arr[j] == arr[j+1]:
                    break
                else:
                    flag += 1
            if flag == length-1:
                arr[length-1], arr[length-2] = arr[length-2], arr[length-1]
            cnt += 1
    b = ''
    for j in range(length):
        b += arr[j]
    print('#%d' %i, b)