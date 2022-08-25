def start():
    global q, ans, visited
    while q:
        x, y = q.pop(0)
        if y == g:
            ans = x
            break
        for i in range(v+1):
            if arr[y][i] == 1 and visited[i] == 0:
                visited[i] = 1
                q.append((x+1, i))


t = int(input())
for i in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[0] * (v+1) for _ in range(v+1)]
    for j in range(e):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    s, g = map(int, input().split())
    ans = 0
    visited = [0] * (v+1)
    q = [(0, s)]
    start()

    print('#%d' %i, ans)