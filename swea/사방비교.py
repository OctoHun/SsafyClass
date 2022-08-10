t = int(input())
for l in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di=[0, 0, 1, -1]
    dj = [-1, 1, 0, 0]
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if 0 <= i+di[k] < N and 0 <= j+dj[k] < N:
                    if arr[i][j] > arr[i+di[k]][j+dj[k]]:
                        ans += arr[i][j] - arr[i+di[k]][j+dj[k]]
                    else:
                        ans += arr[i+di[k]][j+dj[k]] - arr[i][j]
    print('#%d' %l, ans)
