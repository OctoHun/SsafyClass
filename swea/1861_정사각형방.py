def go(a, b):
    global cnt, max, max_room
    for k in range(4):
        ni = di[k]+a
        nj = dj[k]+b
        if 0 <= ni < n and 0 <= nj < n and room[ni][nj]==room[a][b]+1:
            cnt += 1
            go(ni, nj)
            if cnt > max:
                max = cnt
                max_room = start_room
            elif cnt == max and start_room < max_room:
                max_room = start_room
            return


t = int(input())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
for tc in range(1, t+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    max = 0
    max_room = 9999
    for i in range(n):
        for j in range(n):
            cnt = 1
            start_room = room[i][j]
            go(i, j)
    print('#%d' %tc, max_room, max)