t = int(input())
for i in range(1, t+1):
    n, x = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    row = [-1] * n
    col = [-1] * n
    for j in range(n):
        for k in range(n-1):        # 옆 칸이랑 2 이상 차이나면 안됨
            if arr[j][k] - arr[j][k+1] > 1  or arr[j][k+1] - arr[j][k] > 1:
                row[j] = 0
                break
    for j in range(n):
        if row[j] == -1:
            temp = [0] * n
            for k in range(n-1):
                if row[j] == -1:
                    if arr[j][k] - 1 == arr[j][k+1]:
                        for l in range(2, x+1):
                            if k+x > n-1 or arr[j][k+1] != arr[j][k+l]:
                                row[j] = 0
                                break
                        else:
                            temp[k+x] = 1
                    elif arr[j][k] + 1 == arr[j][k+1]:
                        for l in range(1, x):
                            if k-x+1 < 0 or arr[j][k] != arr[j][k-l] or temp[k] == 1 or temp[k-l] == 1:
                                row[j] = 0
                                break
    for j in range(n):
        for k in range(n-1):        # 옆 칸이랑 2 이상 차이나면 안됨
            if arr[k][j] - arr[k+1][j] > 1 or arr[k+1][j] - arr[k][j] > 1:
                col[j] = 0
                break
    for j in range(n):
        if col[j] == -1:
            temp = [0] * n
            for k in range(n-1):
                if col[j] == -1:
                    if arr[k][j] - 1 == arr[k+1][j]:
                        for l in range(2, x+1):
                            if k+x > n-1 or arr[k+1][j] != arr[k+l][j]:
                                col[j] = 0
                                break
                        else:
                            temp[k+x] = 1
                    elif arr[k][j] + 1 == arr[k+1][j]:
                        for l in range(1, x):
                            if k-x+1 < 0  or arr[k][j] != arr[k-l][j] or temp[k] == 1 or temp[k-l] == 1:
                                col[j] = 0
                                break
    cnt = 0
    for j in range(n):
        if row[j] == -1:
            cnt += 1
        if col[j] == -1:
            cnt += 1
    print('#%d' %i, cnt)