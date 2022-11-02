import sys
from collections import deque

def bfs(x):
    for i in range(1, n+1):
        if relation[x][i] != 0:



n, m = map(int, sys.stdin.readline().split())
relation = [[] for _ in range(n+1)]
q = deque()
for i in range(m):
    a = list(map(int, sys.stdin.readline().split()))
    relation[a[0]].append(a[1])
    relation[a[1]].append(a[0])
print(relation)
# for i in range(1, n+1):
#     bfs(i)