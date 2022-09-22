def sumfunc(result, y, x):
    global min
    if y+x == (n-1)*2:
        if result < min:
            min = result
        return
    if y < n-1:
        sumfunc(result+arr[y+1][x], y+1, x)
    if x < n-1:
        sumfunc(result+arr[y][x+1], y, x+1)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min = 999999
    sumfunc(arr[0][0], 0, 0)
    print('#%d' %tc, min)