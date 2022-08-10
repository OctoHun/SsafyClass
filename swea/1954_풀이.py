T = int(input())

for tc in range(1, T+1):
    n = int(input())
    di = [0, 1, 0, -1] # 우 하 좌 상
    dj = [1, 0, -1, 0]
    d = 0
    snail = [[0] * n for _ in range(n)]
    value = 1
    ci, cj = 0, 0
    snail[ci][cj] = value

    while value < n*n:
        ni = ci + di[d]
        nj = cj + dj[d]
        for i in range(4):
            d = (d+i) % 4
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0 <= ni < n and 0 <= nj < n and snail[ni][nj] == 0:
                ci = ni
                cj = nj
                break;
        value += 1
        snail[ci][cj] = value
    print(f"#{tc}")
    for i in range(n):
        for j in range(n):
            print(snail[i][j] , end=" ")
        print()
