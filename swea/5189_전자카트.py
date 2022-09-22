def cart(result, y, cnt):
    global min
    if cnt == n:
        if result+arr[y][0] < min:
            min = result+arr[y][0]
        return
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            cart(result + arr[y][i], i, cnt+1)
            visit[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * n
    visit[0] = 1
    min = 999999
    cart(0, 0, 1)
    print('#%d' %tc, min)