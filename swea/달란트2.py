t = int(input())
for i in range(1, t+1):
    n, p = map(int, input().split())
    ans = 1
    a = n//p
    b = n%p
    if b == 0:
        for j in range(p):
            ans *= a
    else:
        for j in range(b):
            ans *= (a + 1)
        for j in range(p - b):
            ans *= a
    print('#%d' %i, ans)