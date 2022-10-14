from collections import deque
n, m = map(int, input().split())
arrn = [list(input()) for _ in range(n)]
arrm = [list(input()) for _ in range(m)]
arrn.sort()
arrm.sort()
now = 0
same = deque()
for i in range(m):
    for j in range(now, n):
        if arrm[i]==arrn[j]:
            now = j+1
            same.append(arrm[i])
for i in same:
    print(i.join())