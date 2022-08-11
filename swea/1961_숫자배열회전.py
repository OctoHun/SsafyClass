t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    turn90 = [[0]*n for _ in range(n)]
    turn180 = [[0]*n for _ in range(n)]
    turn270 = [[0]*n for _ in range(n)]
    print('#%d' %i)
    for j in range(n):
        for k in range(n):
            turn90[k][n-1-j]=arr[j][k]
            turn180[n-1-j][n-1-k] = turn90[k][n-1-j]
            turn270[n-1-k][j] = turn180[n-1-j][n-1-k]
    for j in range(n):
        for k in range(n):
            print(turn90[j][k], end = '')
        print(end = ' ')
        for k in range(n):
            print(turn180[j][k], end = '')
        print(end = ' ')
        for k in range(n):
            print(turn270[j][k], end = '')
        print()