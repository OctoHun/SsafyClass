import sys
from collections import deque

def bfs():
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    while q:
        y, x, cnt = q.popleft()
        if y == n-1 and x == m-1:
            return cnt
        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]
            if 0 <= ni < m and 0 <= nj < n and visited[nj][ni] == 0 and arr[nj][ni] == 1:
                visited[nj][ni] = 1
                q.append((nj, ni, cnt+1))


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
q = deque()
q.append((0, 0, 1))
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
ans = bfs()
print(ans)