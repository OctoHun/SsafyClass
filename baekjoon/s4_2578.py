bingo = [list(map(int, input().split())) for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        flag1 = 0
        for a in range(5):
            for b in range(5):
                if bingo[a][b] == arr[i][j]:
                    bingo[a][b] = 0
                    flag1 = 1
                    break
            if flag1 == 1:
                break
        for a in range(5):
            for b in range(5):
                if

