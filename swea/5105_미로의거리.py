def start():
    global ans
    while q:
        cnt, y, x = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = y + di
            nj = x + dj
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                if maze[ni][nj] == 2:
                    ans = cnt
                    return
                visited[ni][nj] = 1
                q.append((cnt+1, ni, nj))


t = int(input())
for i in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    q = []
    si = -1
    for j in range(n):
        for k in range(n):
            if maze[j][k] == 3:
                si = j
                sj = k
                break
        if si != -1:
            break
    q.append((0, si, sj))
    visited = [[0] * n for _ in range(n)]
    ans = 0
    start()
    print('#%d' %i, ans)