def kill(time):
    global ans
    if time == m:
        ans = 0
        for i in range(k):
            ans += cell[i][2]
        return
    for i in range(k):
        if cell[i][2] != 0:
            if cell[i][3] == 1:
                cell[i][0] -= 1
            elif cell[i][3] == 2:
                cell[i][0] += 1
            elif cell[i][3] == 3:
                cell[i][1] -= 1
            elif cell[i][3] == 4:
                cell[i][1] += 1
            if cell[i][0] == 0 or cell[i][1] == 0 or cell[i][0] == n-1 or cell[i][1] == n-1:
                if cell[i][3] % 2 == 0:
                    cell[i][3] -= 1
                else:
                    cell[i][3] += 1
                cell[i][2] = cell[i][2]//2

    for i in range(k):
        if cell[i][2] != 0:
            same_index = [0] * k
            max_index = i
            max = cell[i][2]
            for j in range(i+1, k):
                if cell[i][0] == cell[j][0] and cell[i][1] == cell[j][1]:
                    same_index[j] = 1
                    if cell[j][2] > max:
                        same_index[max_index] = 1
                        same_index[j] = 0
                        max_index = j
                        max = cell[j][2]
            for j in range(k):
                if same_index[j] == 1:
                    cell[max_index][2] += cell[j][2]
                    cell[j][2] = 0
    kill(time+1)


t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    cell = [list(map(int, input().split())) for _ in range(k)]
    arr = [[0] * n for _ in range(n)]
    ans = 0
    # 1: 상, 2: 하, 3: 좌, 4: 우
    kill(0)
    print('#%d' %tc, ans)