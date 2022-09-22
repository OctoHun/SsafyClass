def p(i, k):
    global min_V
    if i == k:
        pl.insert(0, 1)
        pl.insert(N, 1)
        temp = 0
        for j in range(N):
            temp += arr[pl[j]-1][pl[j+1]-1]
        if temp < min_V:
            min_V = temp
        return
    else:
        for x in range(M):
            if not used[x]:
                used[x] = 1
                pl[i] = perm[x]
                p(i+1, k)
                used[x] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    perm = [i for i in range(2, N+1)]
    M = len(perm)
    used = [0]*M
    pl = [0]*M
    min_V = 100*N

    p(0, M)
    print(min_V)