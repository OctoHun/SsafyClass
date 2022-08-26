n = int(input())
arr = [[-1] * 1001 for _ in range(1001)]
square = [list(map(int, input().split())) for _ in range(n)]
cnt = [0] * n
for i in range(n):
    for j in range(square[i][0], square[i][0] + square[i][2]):
        for k in range(square[i][1], square[i][1] + square[i][3]):
            if arr[j][k] != -1:
                cnt[arr[j][k]] -= 1
            arr[j][k] = i
            cnt[i] += 1
for i in cnt:
    print(i)