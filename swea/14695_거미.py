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
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    a = y[i]*(z[j]-z[k]) + y[j]*(z[k]-z[i]) + y[k]*(z[i]-z[j])
                    b = z[i]*(x[j]-x[k]) + z[j]*(x[k]-x[i]) + z[k]*(x[i]-x[j])
                    c = x[i]*(y[j]-y[k]) + x[j]*(y[k]-y[i]) + x[k]*(y[i]-y[j])
                    d = x[i]*(y[j]*z[k] - y[k]*z[j]) + x[j]*(y[k]*z[i] - y[i]*z[k]) + x[k]*(y[i]*z[j] - y[j]*z[i])
                    if a != 0 and b != 0 and c != 0:
                        flag = 1
                        break
                    if k == n-1:
                        flag = 2
                        break
                if flag > 0:
                    break
            if flag > 0:
                break
        if flag == 1:
            for i in range(k+1, n):
                func = a*x[i] + b*y[i] + c*z[i]
                if func != d:
                    ans = 'NIE'
                    break
    print('#%d' %tc, ans)