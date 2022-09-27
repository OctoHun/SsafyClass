def check(y, x):
    for i in range(n):
        board[y][i] += 1
        board[i][x] += 1
        if y-i >= 0:
            if x-i >= 0:
                board[y-i][x-i] += 1
            if x+i < n:
                board[y-i][x+i] += 1
        if y+i < n:
            if x-i >= 0:
                board[y+i][x-i] += 1
            if x+i < n:
                board[y+i][x+i] += 1
    board[y][x] -= 5


def uncheck(y, x):
    for i in range(n):
        board[y][i] -= 1
        board[i][x] -= 1
        if y-i >= 0:
            if x-i >= 0:
                board[y-i][x-i] -= 1
            if x+i < n:
                board[y-i][x+i] -= 1
        if y+i < n:
            if x-i >= 0:
                board[y+i][x-i] -= 1
            if x+i < n:
                board[y+i][x+i] -= 1
    board[y][x] += 5


def chess(queen):
    global cnt
    if queen == n:
        cnt += 1
        return
    for i in range(n):
        if board[queen][i] == 0:
            check(queen, i)
            chess(queen+1)
            uncheck(queen, i)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    cnt = 0
    chess(0)
    print('#%d' %tc, cnt)