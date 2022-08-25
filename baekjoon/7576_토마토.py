def tomato():
    global q, arr, visited, ans
    while q:
        day, i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = di + i
            nj = dj + j
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                arr[ni][nj] = 1
                q.append((day+1, ni, nj))
        ans = day


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = []
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((0, i, j))
            visited[i][j] = 1
ans = 0
tomato()
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            ans = -1
            break
    if ans == -1:
        break
print(ans)