def start(arr, a, b):
    global ans
    if a == b:
        ans = 1
        return
    for i in range(2):
        if arr[a][i] != -1:
            if arrive[arr[a][i]] == 0:
                arrive[arr[a][i]] = 1
                start(arr, arr[a][i], b)
                arrive[arr[a][i]] = 0
    return



for i in range(1, 11):
    arr = [[-1] * 2 for _ in range(100)]
    arrive = [0] * 100
    arrive[0] = 1
    t, n = map(int, input().split())
    road = list(map(int, input().split()))
    for j in range(n):
        if arr[road[2*j]][0] == -1:
            arr[road[2*j]][0] = road[2*j+1]
        else:
            arr[road[2*j]][1] = road[2*j+1]
    ans = 0
    start(arr, 0, 99)
    print('#%d' %i, ans)