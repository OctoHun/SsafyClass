def check(arr):
    cnt = 0
    for i in range(10):
        if arr[i] >= 3:
            return 1
        elif arr[i] >= 1:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            return 1
    return 0


t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    ans = 0
    for i in range(0, 4, 2):
        player1[arr[i]] += 1
        player2[arr[i+1]] += 1
    for i in range(4, 12, 2):
        player1[arr[i]] += 1
        player2[arr[i+1]] += 1
        a = check(player1)
        if a:
            ans = 1
            break
        b = check(player2)
        if b:
            ans = 2
            break
    print('#%d' %tc, ans)