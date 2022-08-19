for i in range(1, 11):
    t = int(input())
    arr = list(map(int, input().split()))
    d = [1, 2, 3, 4, 5]
    temp = [0] * 5
    flag = 1
    print('#%d' %i, end = ' ')
    while flag == 1:
        for j in range(5):
            arr[j] -= d[j]
            temp[j] = arr[j]
            if arr[j] <= 0:
                arr[j] = 0
                flag = 0
                break
        if flag == 1:
            arr[0] = arr[5]
            arr[1] = arr[6]
            arr[2] = arr[7]
            for k in range(5):
                arr[3+k] = temp[k]
    for k in range(j+1, 8):
        print(arr[k], end = ' ')
    for k in range(0, j+1):
        print(arr[k], end = ' ')
    print()