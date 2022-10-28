import sys
def find_set(x):
    while x != arr[x]:
        x = arr[x]
    return x


n, m = map(int, sys.stdin.readline().split())
arr = [0] * (n+1)
cnt = 0
for i in range(n+1):
    arr[i] = i
for i in range(m):
    a = list(map(int, sys.stdin.readline().split()))
    arr[find_set(a[0])] = find_set(a[1])
for i in range(n+1):
    if arr[i] == i:
        cnt += 1
print(cnt-1)