import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(i+1):
        if j-1 >= 0:
            if j < i:
                arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
            else:
                arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += arr[i-1][j]
ans = 0
for i in range(n):
    if ans < arr[n-1][i]:
        ans = arr[n-1][i]
print(ans)