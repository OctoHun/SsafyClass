import sys
from collections import deque

def bfs(target):
    while q:
        y = q.popleft()
        for i in range(n):
            if arr[y][i] == 1:
                q.append(i)
                ans[y][i] = 1


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [0] * (n+1)
ans = [[0]*n for _ in range(n)]
q = deque()
for i in range(n):
    q.append(i)
    bfs(target)