def factory(fee, cnt):
    global min
    if cnt == n:
        if fee < min:
            min = fee
        return
    if fee >= min:
        return
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            factory(fee+arr[cnt][i], cnt+1)
            visit[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min = 999999
    visit = [0] * n
    factory(0, 0)
    print('#%d' %tc, min)