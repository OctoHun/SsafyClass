t = int(input())
arr = [[0] * 11 for _ in range(11)]
for i in range(1, t+1):
    n = int(input())
    print('#%d' %i, end = ' ')
    for i in range(n+1):
        for j in range(i):
            if j == 0:
                arr[i][j] = 1
            elif i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
            print(arr[i][j], end = ' ')
        print()