square = [list(map(int, input().split())) for _ in range(4)]
arr = [[0] * 100 for _ in range(100)]
for i in range(4):
    square[i][2] -= 1
    square[i][3] -= 1
for i in range(4):
    for j in range(square[i][0], square[i][2]+1):
        for k in range(square[i][1], square[i][3]+1):
            arr[j][k] = 1
cnt = 0
for j in range(100):
    for k in range(100):
        if arr[j][k] == 1:
            cnt += 1
print(cnt)