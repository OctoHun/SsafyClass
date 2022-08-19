t = int(input())
for i in range(1, t+1):
    n = int(input())
    cnt = [0] * 401
    for j in range(n):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        if a % 2 == 0:
            a -= 1
        if b % 2 == 1:
            b += 1
        for k in range(a, b+1):
            cnt[k] += 1
    max = 0
    for j in range(401):
        if cnt[j] > max:
            max = cnt[j]
    print('#%d' %i, max)