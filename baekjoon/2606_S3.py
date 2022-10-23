import sys
def find_set(x):
    while x != arr[x]:
        x = arr[x]
    return x


n = int(sys.stdin.readline())
arr = [0]*(n+1)
for i in range(n+1):
    arr[i] = i
m = int(sys.stdin.readline())
cnt = 0
for i in range(m):
    a = list(map(int, sys.stdin.readline().split()))
    if find_set(a[1]) == 1:
        arr[find_set(a[0])] = find_set(a[1])
    else:
        arr[find_set(a[1])] = find_set(a[0])
for i in range(n+1):
    if find_set(arr[i]) == 1:
        cnt += 1
print(cnt-1)