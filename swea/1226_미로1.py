def bfs(si, sj):   # g: 그래프, start: 시작지점, n: 정점개수
    global ans
    # 중복 탐색 방지를 위한 방문 배열
    visited = [[0] * n for _ in range(n)]
    q = []
    visited[si][sj] = 1
    q.append((si, sj))

    while q:
        i, j = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 16 and 0 <= nj < 16:
                if maze[ni][nj] == 3:
                    ans = 1
                    return
                elif maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))



for i in range(1, 11):
    t = int(input())
    n = 16
    maze = [list(map(int, input())) for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if maze[j][k] == 2:
                si = j
                sj = k
                break
    ans = 0
    bfs(si, sj)
    print('#%d' %i, ans)