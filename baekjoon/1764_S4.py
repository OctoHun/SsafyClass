import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
arrn = dict()
ans = deque()
for i in range(n):
    a = sys.stdin.readline().rstrip()
    arrn[a] = 1
arrm = [sys.stdin.readline().rstrip() for _ in range(m)]
arrm.sort()
for i in range(m):
    if arrn.get(arrm[i]) == None:
        pass
    else:
        ans.append(arrm[i])
print(len(ans))
for i in ans:
    print(i)