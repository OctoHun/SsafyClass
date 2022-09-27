def work(cnt, ans):
    global max
    if cnt == n:
        if ans > max:
            max = ans
        return
    if ans <= max:
        return
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            work(cnt+1, ans*arr[cnt][i]/100)
            visit[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    max = 0
    work(0, 1)
    max *= 100
    print('#%d %6f' %(tc, max))