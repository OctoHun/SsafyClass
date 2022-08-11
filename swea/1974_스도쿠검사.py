t = int(input())
for i in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for j in range(9):
        temp_row = [0] * 10
        temp_col = [0] * 10
        for k in range(9):
            temp_row[arr[j][k]] += 1
            temp_col[arr[k][j]] += 1
        for k in range(1, 10):
            if temp_row[k] == 0 or temp_col[k] == 0:
                ans = 0
                break
        if ans == 0:
            break
    for j in range(0, 9, 3):
        for k in range(0, 9, 3):
            temp = [0] * 10
            for a in range(3):
                for b in range(3):
                    temp[arr[j+a][k+b]] += 1
            for c in range(1, 10):
                if temp[c] == 0:
                    ans = 0
                    break
                if ans == 0:
                    break
            if ans == 0:
                break
        if ans == 0:
            break




    print('#%d' %i, ans)