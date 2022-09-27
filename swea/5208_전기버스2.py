def bus(elect, now, cnt):
    global min
    if now == arr[0]:
        if cnt < min:
            min = cnt
        return
    if cnt >= min:
        return
    for i in range(1, elect+1):
        if now+i <= arr[0]:
            bus(arr[now+i], now+i, cnt+1)


t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    arr.append(0)
    min = 99999
    bus(arr[1], 1, 0)
    print('#%d' %tc, min-1)