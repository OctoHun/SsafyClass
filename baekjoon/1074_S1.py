def dfs(ys, xs, ye, xe, cnt):
    global ans
    if cnt == n:
        return
    if ys <= r < (ys+ye)//2:
        if xs <= c < (xs+xe)//2:
            dfs(ys, xs, (ys+ye)//2, (xs+xe)//2, cnt+1)
        else:
            ans += ((ye-ys)//2)**2
            dfs(ys, (xs+xe)//2, (ys+ye)//2, xe, cnt+1)
    else:
        if xs <= c < (xs+xe)//2:
            ans += ((ye-ys)//2)**2 * 2
            dfs((ys+ye)//2, xs, ye, (xs+xe)//2, cnt+1)
        else:
            ans += ((ye-ys)//2)**2 * 3
            dfs((ys+ye)//2, (xs+xe)//2, ye, xe, cnt+1)



n, r, c = map(int, input().split())
length = 2**n
ans = 0
dfs(0, 0, length, length, 0)
print(ans)