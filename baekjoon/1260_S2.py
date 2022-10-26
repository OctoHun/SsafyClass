import sys
from collections import deque

def dfs(x):
    print(x, end = ' ')
    for i in range(n+1):
        if arr[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


def bfs():
    while q:
        target = q.popleft()
        for i in range(n+1):
            if arr[target][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append(i)
                print(i, end= ' ')


n, m, v = map(int, sys.stdin.readline().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a = list(map(int, sys.stdin.readline().split()))
    arr[a[0]][a[1]] = 1
    arr[a[1]][a[0]] = 1
q = deque()
visited = [0]*(n+1)
visited[v] = 1
dfs(v)
print()
visited = [0]*(n+1)
visited[v] = 1
q.append(v)
print(v, end = ' ')
bfs()