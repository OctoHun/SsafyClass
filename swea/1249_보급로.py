from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
def func():
    q = deque()
    q.append([0, 0])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ni = y + di[i]
            nj = x + dj[i]
            if 0 <= ni < n and 0 <= nj < n:
                if ground[ni][nj] > ground[y][x]+arr[ni][nj]:
                    ground[ni][nj] = ground[y][x]+arr[ni][nj]
                    q.append([ni, nj])


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    ground = [[99999]*n for _ in range(n)]
    ground[0][0] = 0
    func()
    print('#%d' %tc, ground[n-1][n-1])