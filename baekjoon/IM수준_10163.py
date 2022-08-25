n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
square = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(square[i][0], square[i][2]+1):
        for k in range(square[i][1], square[i][3]+1):
                arr[j][k] = i+1
for i in range(n):
    cnt = 0
    for j in range(1001):
        for k in range(1001):
            if arr[j][k] == i+1:
                cnt += 1
    print(cnt)
