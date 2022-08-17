t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    print('#%d' %i)
    for j in range(n):
        arr[j][0] = 1
        arr[j][j] = 1
    for j in range(2, n):
        for k in range(1, j):
            arr[j][k] = arr[j-1][k-1] + arr[j-1][k]
    for j in range(n):
        for k in range(n):
            if arr[j][k] != 0:
                print(arr[j][k], end = ' ')
        print()