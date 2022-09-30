def sum_func(a, b):
    global min
    for i in range(n):
        for j in range(n):
            if i in selected and j in selected:
                a += arr[i][j]
            elif i not in selected and j not in selected:
                b += arr[i][j]
    if abs(a-b) < min:
        min = abs(a-b)


def select(cnt, now):
    if cnt == n//2:
        sum_func(0, 0)
        return
    for i in range(now, n):
        selected[cnt] = i
        select(cnt+1, i+1)
        selected[cnt] = -1


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min = 99999
    selected = [-1]*8
    select(0, 0)
    print('#%d' %tc, min)