def dijkstra(k):
    length[0] = 0
    cnt = 0
    while cnt < n+1:
        temp = [0] * (n + 1)
        min = 99999
        for i in range(n+1):
            if road[k][i] != 0 and length[i] > length[k] + road[k][i]:
                length[i] = length[k] + road[k][i]
            if  det[i] == 0 and length[i] < min:
                min_index = i
                min = length[i]
        det[min_index] = 1
        k = min_index
        cnt += 1



t = int(input())
for tc in range(1, t+1):
    n, e = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(e)]
    road = [[0]*(n+1) for _ in range(n+1)]
    for i in range(e):
        road[arr[i][0]][arr[i][1]] = arr[i][2]
    length = [99999]*(n+1)
    det = [0] * (n+1)
    dijkstra(0)
    print('#%d' %tc, length[n])