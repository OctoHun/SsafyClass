import sys
n, m = map(int, sys.stdin.readline().split())
ans = dict()
for i in range(n):
    arr = list(sys.stdin.readline().split())
    ans[arr[0]] = arr[1]
for i in range(m):
    target = input()
    print(ans[target])