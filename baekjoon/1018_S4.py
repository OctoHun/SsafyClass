n, m = map(int, input().split())
min = 999999
board = [list(input()) for _ in range(n)]
for i in range(n-7):
    for j in range(m-7):
        wb = 0
        bw = 0
        for k in range(8):
            for l in range(8):
                if k%2 == 0:
                    if l%2 == 0:
                        if board[i+k][j+l] == 'W':
                            bw += 1
                        else:
                            wb += 1
                    else:
                        if board[i+k][j+l] == 'W':
                            wb += 1
                        else:
                            bw += 1
                else:
                    if l % 2 == 0:
                        if board[i + k][j + l] == 'W':
                            wb += 1
                        else:
                            bw += 1
                    else:
                        if board[i + k][j + l] == 'W':
                            bw += 1
                        else:
                            wb += 1
        if wb < min:
            min = wb
        if bw < min:
            min = bw
print(min)