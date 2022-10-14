import sys
n, m = map(int, input().split())
mon = dict()
for i in range(n):
    a = sys.stdin.readline().rstrip()
    mon[a] = str(i+1)
    mon[str(i+1)] = a
b = [sys.stdin.readline().rstrip() for _ in range(m)]
for i in range(m):
    print(mon[b[i]])