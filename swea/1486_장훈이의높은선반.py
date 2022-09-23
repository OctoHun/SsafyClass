def height(now, result):
    global tower
    if result < b:
        return
    elif result < tower:
        tower = result
    if tower == b:
        return
    for i in range(now, n):
        height(i+1, result-h[i])
        if tower == b:
            return
        height(i+1, result)
        if tower == b:
            return


t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    s = sum(h)
    tower = s
    height(0, s)
    print('#%d' %tc, tower-b)
