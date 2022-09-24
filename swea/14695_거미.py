t = int(input())
for tc in range(1, t+1):
    n = int(input())
    x = [0] * n
    y = [0] * n
    z = [0] * n
    flag = 0
    ans = 'TAK'
    for i in range(n):
        x[i], y[i], z[i] = map(int, input().split())
    if n > 3:
        # 평면의 방정식 ax + by + cz + d = 0
        # a = y1(z2-z3) + y2(z3-z1) + y3(z1-z2)
        # b = z1(x2-x3) + z2(x3-x1) + z3(x1-x2)
        # c = x1(y2-y3) + x2(y3-y1) + x3(y1-y2)
        # d = -x1(y2z3-y3z2) - x2(y3z1-y1z3) - x3(y1z2-y2z1)
        # 점과 평면사이의 거리 d = (ax + by + cz + d) / sqrt(a^2 + b^2 + c^2)

        for k in range(2, n):
            a = y[0]*(z[1]-z[k]) + y[1]*(z[k]-z[0]) + y[k]*(z[0]-z[1])
            b = z[0]*(x[1]-x[k]) + z[1]*(x[k]-x[0]) + z[k]*(x[0]-x[1])
            c = x[0]*(y[1]-y[k]) + x[1]*(y[k]-y[0]) + x[k]*(y[0]-y[1])
            d = x[0]*(y[1]*z[k] - y[k]*z[1]) + x[1]*(y[k]*z[0] - y[0]*z[k]) + x[k]*(y[0]*z[1] - y[1]*z[0])
            if a != 0 and b != 0 and c != 0:
                flag = 1
                break
        if flag == 1:
            for i in range(k+1, n):
                func = a*x[i] + b*y[i] + c*z[i]
                if func != d:
                    ans = 'NIE'
                    break
    print('#%d' %tc, ans)