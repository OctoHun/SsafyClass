n = int(input())
cnt = 0
arr = [[0] * 100 for _ in range(100)]
paper = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(paper[i][0], paper[i][0]+10):
        for k in range(paper[i][1], paper[i][1]+10):
            arr[j][k] = 1
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)