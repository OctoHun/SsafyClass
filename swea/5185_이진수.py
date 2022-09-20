t = int(input())
for tc in range(1, t+1):
    n, s = input().split()
    n = int(n)
    ans = ''
    for i in range(n):
        num = int(s[i], 16)
        for j in range(3, -1, -1):
            if num & (1<<j):
                ans += '1'
            else:
                ans += '0'
    print('#%d' %tc, ans)