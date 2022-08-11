t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ans = 0
    for j in range(1 << 12):
        cnt = 0
        sum = 0
        for l in range(12):
            if j & (1 << l):
                cnt += 1
                sum += a[l]
        if cnt == n and sum == k:
            ans += 1
    print('#%d' %i, ans)