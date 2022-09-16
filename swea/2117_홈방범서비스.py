t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    home_map = [list(map(int, input().split())) for _ in range(n)]
    homex = []
    homey = []
    home = 0
    flag = 0
    ans = [0] * 100000
    q = 0
    for i in range(n):
        for j in range(n):
            if home_map[i][j] == 1:
                homey.append(i)
                homex.append(j)
                home += 1

    for i in range(n):
        for j in range(n):
            for k in range(n+5, 0, -1):
                cost = k*k + (k-1)*(k-1)
                cnt = 0
                for l in range(home):
                    if abs(homey[l]-i)+abs(homex[l]-j)+1 <= k:
                        cnt += 1
                if cnt*m >= cost:
                    ans[q] = cnt
                    q += 1
            if flag == 1:
                break
        if flag == 1:
            break
    max = 0
    for i in range(q):
        if max < ans[i]:
            max = ans[i]
    print('#%d' %tc, max)