t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    for i in range(m):
        arr[i][0], arr[i][1] = arr[i][1]-1, arr[i][0]-1
    board = [[0]*n for _ in range(n)]
    board[n//2-1][n//2-1] = 2
    board[n//2][n//2] = 2
    board[n//2-1][n//2] = 1
    board[n//2][n//2-1] = 1
    white = 2
    black = 2
    for i in range(m):
        y = arr[i][0]
        x = arr[i][1]
        z = arr[i][2]
        board[y][x] = z
        if z == 1:
            black += 1
        else:
            white += 1
        cnt = 0
        flag = 0
        for j in range(y-1, -1, -1): # 위쪽
            if board[j][x] == z:
                flag = 1
                break
            elif board[j][x] == 0:
                break
            else:
                cnt += 1
        if flag == 1 and cnt > 0:
            for j in range(cnt):
                board[y-j-1][x] = z
            if z == 1:
                black += cnt
                white -= cnt
            else:
                black -= cnt
                white += cnt
        cnt = 0
        flag = 0
        for j in range(y+1, n): # 아래쪽
            if board[j][x] == z:
                flag = 1
                break
            elif board[j][x] == 0:
                break
            else:
                cnt += 1
        if flag == 1 and cnt > 0:
            for j in range(cnt):
                board[y+j+1][x] = z
            if z == 1:
                black += cnt
                white -= cnt
            else:
                black -= cnt
                white += cnt
        cnt = 0
        flag = 0
        for j in range(x+1, n): # 오른쪽
            if board[y][j] == z:
                flag = 1
                break
            elif board[y][j] == 0:
                break
            else:
                cnt += 1
        if flag == 1 and cnt > 0:
            for j in range(cnt):
                board[y][x+1+j] = z
            if z == 1:
                black += cnt
                white -= cnt
            else:
                black -= cnt
                white += cnt
        cnt = 0
        flag = 0
        for j in range(x-1, -1, -1): # 왼쪽
            if board[y][j] == z:
                flag = 1
                break
            elif board[y][j] == 0:
                break
            else:
                cnt += 1
        if flag == 1 and cnt > 0:
            for j in range(cnt):
                board[y][x-1-j] = z
            if z == 1:
                black += cnt
                white -= cnt
            else:
                black -= cnt
                white += cnt
        cnt = 0
        flag = 0
        for j in range(n):  # 왼쪽 위 대각선
            if y-j-1 >= 0 and x-j-1 >= 0 and board[y-j-1][x-j-1] == z:
                flag = 1
                break
            elif y-j-1 >= 0 and x-j-1 >= 0 and board[y-j-1][x-j-1] == 0:
                break
            elif y-j-1 >= 0 and x-j-1 >= 0:
                cnt += 1
            else:
                break
        if flag == 1 and cnt > 0:
            for j in range(cnt):
                board[y-j-1][x - 1 - j] = z
            if z == 1:
                black += cnt
                white -= cnt
            else:
                black -= cnt
                white += cnt
        cnt = 0
        flag = 0
        for j in range(n):  # 오른쪽 위 대각선
            if y - j - 1 >= 0 and x + j + 1 < n and board[y - j - 1][x + j + 1] == z:
                flag = 1
                break
            elif y - j - 1 >= 0 and x + j + 1 < n and board[y - j - 1][x + j + 1] == 0:
                break
            elif y - j - 1 >= 0 and x + j + 1 < n:
                cnt += 1
            else:
                break
        if flag == 1 and cnt > 0:
            for j in range(cnt):
                board[y - j - 1][x + 1 + j] = z
            if z == 1:
                black += cnt
                white -= cnt
            else:
                black -= cnt
                white += cnt
        cnt = 0
        flag = 0
        for j in range(n):  # 왼쪽 아래 대각선
            if y + j + 1 < n and x - j - 1 >= 0 and board[y + j + 1][x - j - 1] == z:
                flag = 1
                break
            elif y + j + 1 < n and x - j - 1 >= 0 and board[y + j + 1][x - j - 1] == 0:
                break
            elif y + j + 1 < n and x - j - 1 >= 0:
                cnt += 1
            else:
                break
        if flag == 1 and cnt > 0:
            for j in range(cnt):
                board[y + j + 1][x - 1 - j] = z
            if z == 1:
                black += cnt
                white -= cnt
            else:
                black -= cnt
                white += cnt
        cnt = 0
        flag = 0
        for j in range(n):  # 오른쪽 아래 대각선
            if y + j + 1 < n and x + j + 1 < n and board[y + j + 1][x + j + 1] == z:
                flag = 1
                break
            elif y + j + 1 < n and x + j + 1 < n and board[y + j + 1][x + j + 1] == 0:
                break
            elif y + j + 1 < n and x + j + 1 < n:
                cnt += 1
            else:
                break
        if flag == 1 and cnt > 0:
            for j in range(cnt):
                board[y + j + 1][x + j + 1] = z
            if z == 1:
                black += cnt
                white -= cnt
            else:
                black -= cnt
                white += cnt
    print('#%d' %tc, black, white)