t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    board = [[0]*n for _ in range(n)]
    board[n//2-1][n//2-1] = 2
    board[n//2][n//2] = 2
    board[n//2-1][n//2] = 1
    board[n//2][n//2-1] = 1
    white = 2
    black = 2
    di = [0, 0, 1, -1, 1, 1, -1, -1]
    dj = [-1, 1, 0, 0, 1, -1, 1, -1]
    for i in range(m):
        y = arr[i][1]-1
        x = arr[i][0]-1
        z = arr[i][2]
        board[y][x] = z
        if z == 1:
            black += 1
        else:
            white += 1
        for j in range(8):
            cnt = 0
            flag = 0
            for k in range(1, n):
                ni = di[j]*k + y
                nj = dj[j]*k + x
                if 0 <= ni < n and 0 <= nj < n:
                    if board[ni][nj] == 0:
                        break
                    elif board[ni][nj] == z:
                        flag = 1
                        break
                    else:
                        cnt += 1
            if flag == 1 and cnt > 0:
                for k in range(cnt):
                    board[y+(di[j]*(k+1))][x+(dj[j]*(k+1))] = z
                if z == 2:
                    white += cnt
                    black -= cnt
                else:
                    white -= cnt
                    black += cnt
    print('#%d' %tc, black, white)