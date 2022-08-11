for i in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    now = [0, 0]
    cnt1 = 0
    for j in range(100):
        if arr[99][j] == 2:
            target = j
        if arr[0][j] == 1:
            cnt1 += 1
    start_arr = [0] * cnt1
    cnt2 = 0
    for j in range(100):
        if arr[0][j] == 1:
            start_arr[cnt2] = j
            cnt2 += 1
        if target == j:
            index = cnt2-1
    now[0] = 99
    now[1] = start_arr[index]
    for j in range(99, -1, -1):
        if now[1] != 0 and arr[j][now[1] - 1] == 1:
            index -= 1
            now[1] = start_arr[index]
        elif now[1] != 99 and arr[j][now[1] +1] == 1:
            index += 1
            now[1] = start_arr[index]
        if j == 0:
            ans = now[1]
    print('#%d' %tc, ans)