def findset(k):
    while team[k] != k:
        k = team[k]
    return k


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    team = [0]*(n+1)
    for i in range(n+1):
        team[i] = i
    cnt = 0
    for i in range(0, m*2, 2):
        team[findset(arr[i+1])] = findset(arr[i])
    for i in range(1, n+1):
        if team[i] == i:
            cnt += 1
    print('#%d' %tc, cnt)