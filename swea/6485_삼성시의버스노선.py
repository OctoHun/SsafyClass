t = int(input())
for i in range(1, t+1):
    n = int(input())
    a = [0] * 501
    b = [0] * 501
    c = [0] * 500
    ans = [-1] * 500
    for j in range(1, n+1):
        a[j], b[j] = map(int, input().split())
    p = int(input())
    for j in range(p):
        c[j] = int(input())
        cnt = 0
        for k in range(1, n+1):
            if a[k] <= c[j] <= b[k]:
                cnt+= 1
        ans[j] = cnt
    print('#%d' %i, end = ' ')
    for j in range(500):
        if ans[j] == -1:
            break
        else:
            print(ans[j], end = ' ')
    print()