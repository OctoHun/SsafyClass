import sys
from collections import deque

def bfs(cnt):
    di = [0, 0, 1, -1]
    dj = [-1, 1, 0, 0]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ni = y + di[i]
            nj = x + dj[i]
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
                arr[ni][nj] = 0
                cnt += 1
    return cnt


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
total_cnt = 0
visited = [[0]*n for _ in range(n)]
q = deque()
ans = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            visited[i][j] = 1
            q.append((i, j))
            ans.append(bfs(1))
            total_cnt += 1
ans = list(ans)
ans.sort()
print(total_cnt)
length = len(ans)
for i in range(length):
    print(ans[i])