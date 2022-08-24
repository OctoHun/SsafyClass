def cover():
    global arr
    flag = 1
    for j in range(index):
        a, b, c = ss[j]
        if a == 'A':
            x = 1
        elif a == 'B':
            x = 2
        elif a == 'C':
            x = 3
        for i in range(1, x+1):
            for di, dj in [[0, i], [i, 0], [0, -i], [-i, 0]]:
                ni = b + di
                nj = c + dj
                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'H':
                    arr[ni][nj] = 'X'


t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]
    ss = [0] * 50
    index = 0
    for j in range(n):
        for k in range(n):
            if arr[j][k] != 'X' and arr[j][k] != 'H':
                ss[index] = ((arr[j][k], j, k))
                index += 1
    cover()
    cnt = 0
    for j in range(n):
        for k in range(n):
            if arr[j][k] == 'H':
                cnt += 1
    print('#%d' %i, cnt)