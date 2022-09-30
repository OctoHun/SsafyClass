def dijkstra_go(arr, x, cnt):
    while cnt < m:
        min = 999999
        min_index = -1
        for i in range(1, n+1):
            if go[x][i] > 0 and go_time[i] > go_time[x]+go[x][i]:
                go_time[i] = go_time[x]+go[x][i]
        for i in range(1, n+1):
            if visited[i] == 0 and min > go_time[i]:
                min = go_time[i]
                min_index = i
        visited[min_index] = 1
        x = min_index
        cnt += 1


def dijkstra_back(arr, x, cnt):
    while cnt < m:
        min = 999999
        min_index = -1
        for i in range(1, n+1):
            if back[x][i] > 0 and back_time[i] > back_time[x]+back[x][i]:
                back_time[i] = back_time[x]+back[x][i]
        for i in range(1, n+1):
            if visited[i] == 0 and min > back_time[i]:
                min = back_time[i]
                min_index = i
        visited[min_index] = 1
        x = min_index
        cnt += 1


t = int(input())
for tc in range(1, t+1):
    n, m, x = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    go = [[0]*(n+1) for _ in range(n+1)]
    back = [[0]*(n+1) for _ in range(n+1)]
    go_time = [999999]*(n+1)
    go_time[x] = 0
    back_time = [999999]*(n+1)
    back_time[x] = 0
    for i in range(m):
        go[arr[i][0]][arr[i][1]] = arr[i][2]
        back[arr[i][1]][arr[i][0]] = arr[i][2]
    visited = [0] * (n+1)
    visited[x] = 1
    dijkstra_go(go, x, 0)
    visited = [0] * (n + 1)
    visited[x] = 1
    dijkstra_back(back, x, 0)
    max = 0
    for i in range(1, n+1):
        if i != x and max < go_time[i]+back_time[i]:
            max = go_time[i]+back_time[i]
    print('#%d' %tc, max)