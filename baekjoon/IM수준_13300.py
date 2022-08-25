n, k = map(int, input().split())
arr = [[0] * 2 for _ in range(6)]
for j in range(n):
    s, y = map(int, input().split())
    arr[y-1][s] += 1
cnt = 0
for j in range(6):
    for l in range(2):
        cnt += arr[j][l]//k
        if arr[j][l]%k != 0:
            cnt += 1
print(cnt)