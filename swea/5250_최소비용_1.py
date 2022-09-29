di = [1, 0, 0, -1]
dj = [0, 1, -1, 0]
def dijkstra():
    now = 0
    new = 0
    cnt = 0
    y, x = 0, 0
    while cnt != n**2:
        for i in range(4):
            ni = y+di[i]
            nj = x+dj[i]
            if 0<=ni<n and 0<=nj<n and visit[ni][nj] == 0:
                if arr[ni][nj] > arr[y][x]:
                    plus = arr[ni][nj]-arr[y][x]+1
                else:
                    plus = 1
                if fuel[ni][nj] > fuel[y][x]+plus:
                    fuel[ni][nj] = fuel[y][x]+plus
        min = 9999
        min_index = [-1, -1]
        for i in range(n):
            for j in range(n):
                if visit[i][j] == 0 and fuel[i][j] < min:
                    min = fuel[i][j]
                    min_index = [i, j]
        visit[min_index[0]][min_index[1]] = 1
        y = min_index[0]
        x = min_index[1]
        cnt += 1


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    fuel =[[9999]*n for _ in range(n)]
    fuel[0][0] = 0
    visit = [[0]*n for _ in range(n)]
    dijkstra()
    print('#%d' %tc, fuel[n-1][n-1])
