t = int(input())
for i in range(1, 1+t):
    N = int(input())
    b = [0] * 10
    for j in range(1, 1000000):
        a = list(map(int, str(N * j)))
        cnt = 0
        for k in range(len(a)):
            b[a[k]] += 1
        for k in range(10):
            if b[k]>0:
                cnt += 1
        if cnt>9:
            ans = N * j
            break
    print('#%d' %i, ans)