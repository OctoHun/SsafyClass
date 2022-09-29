di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]

def bfs():
    while q:
        y, x = q.pop(0)
        for i in range(4):
            ni = y + di[i]
            nj = x + dj[i]
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] > arr[y][x]:
                    plus = arr[ni][nj]-arr[y][x]+1
                else:
                    plus = 1
                if fuel[ni][nj] > fuel[y][x]+plus:
                    fuel[ni][nj] = fuel[y][x]+plus
                    q.append((ni, nj))


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    fuel = [[9999]*n for _ in range(n)]
    fuel[0][0] = 0
    q = [(0, 0)]
    bfs()
    print('#%d' %tc, fuel[n-1][n-1])