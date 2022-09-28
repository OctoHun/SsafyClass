def move(s, e):
    global cnt
    if e[0] == n-1 and e[1] == n-1:
        cnt += 1
        return
    if s[0] == e[0]:
        if e[1]+1 < n and arr[e[0]][e[1]+1] == 0:
            move(e, [e[0], e[1]+1])
            if e[0]+1 < n and arr[e[0]+1][e[1]] == 0 and arr[e[0]+1][e[1]+1] == 0:
                move(e, [e[0]+1, e[1]+1])
    elif s[1] == e[1]:
        if e[0] + 1 < n and arr[e[0]+1][e[1]] == 0:
            move(e, [e[0]+1, e[1]])
            if e[1]+1 < n and arr[e[0]][e[1]+1] == 0 and arr[e[0]+1][e[1]+1] == 0:
                move(e, [e[0]+1, e[1]+1])
    else:
        flag = 0
        if e[1] +1 < n and arr[e[0]][e[1]+1] == 0:
            move(e, [e[0], e[1]+1])
            flag += 1
        if e[0]+1 < n and arr[e[0]+1][e[1]] == 0:
            move(e, [e[0]+1, e[1]])
            flag += 1
        if flag == 2 and arr[e[0]+1][e[1]+1] == 0:
            move(e, [e[0]+1, e[1]+1])


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

move([0, 0], [0, 1])
print(cnt)