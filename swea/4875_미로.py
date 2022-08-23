def move(arr, nowi, nowj, before):
    global ans, di, dj
    if arr[nowi][nowj] == 2:
        ans = 1
        return
    for j in range(4):
            if 0 <= nowi + di[j] < n and 0 <= nowj + dj[j] < n and before[nowi + di[j]][nowj + dj[j]] != 1 and arr[nowi + di[j]][nowj + dj[j]] != 1:
                before[nowi + di[j]][nowj + dj[j]] = 1
                move(arr, nowi + di[j], nowj + dj[j], before)
    return


t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    flag = 0
    for j in range(n):
        for k in range(n):
            if arr[j][k] == 3:
                starti = j
                startj = k
                flag = 1
                break
        if flag == 1:
            break

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    ans = 0
    before = [[0] * n for _ in range(n)]
    before[starti][startj] = 1
    move(arr, starti, startj, before)
    print('#%d' %i, ans)