def findset(x):
    while x != rel[x]:
        x = rel[x]
    return x


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    rel = [0]*(n+1)
    cnt = 0
    for i in range(n+1):
        rel[i] = i
    for i in range(m):
        rel[findset(arr[i][1])] = findset(arr[i][0])
    for i in range(1, n+1):
        if rel[i] == i:
            cnt += 1
    print('#%d' %tc, cnt)