def start(s, g, v):
    global arr, ans
    if s == g:
        ans = 1
        return
    for i in range(1, v+1):
        if arr[s][i] == 1:
            start(i, g, v)
    return



t = int(input())
for i in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[0] * (v+1) for _ in range(v+1)]
    for j in range(e):
        a, b = map(int, input().split())
        arr[a][b] = 1
    s, g = map(int, input().split())
    ans = 0
    start(s, g, v)
    print('#%d' %i, ans)