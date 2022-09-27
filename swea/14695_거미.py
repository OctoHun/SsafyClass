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
        x1, x2 = x[0], x[1]
        y1, y2 = y[0], y[1]
        z1, z2 = z[0], z[1]
        fix_x, fix_y, fix_z = 0, 0, 0
        if x2 == x1:
            fix_x = 1
        if y2 == y1:
            fix_y = 1
        if z1 == z2:
            fix_z = 1
        for k in range(2, n):
            if fix_x:
                if fix_y:
                    if x[k] == x1 and y[k] == y2:
                        continue
                elif fix_z:
                    if x[k] == x1 and z[k] == z2:
                        continue
                else:
                    if (y[k]-y1)*(z2-z1) == (y2-y1)*(z[k]-z1) and x[k]==x1:
                        continue
            elif fix_y:
                if fix_z:
                    if y[k] == y1 and z[k] == z2:
                        continue
                else:
                    if (x[k]-x1)*(z2-z1) == (x2-x1)*(z[k]-z1) and y[k]==y1:
                        continue
            elif fix_z:
                if (x[k]-x1) * (y2-y1) == (x2-x1) * (y[k]-y1) and z[k]==z1:
                    continue
            else:
                if (x[k]-x1)*(y2-y1)*(z2-z1) == (y[k]-y1)*(x2-x1)*(z2-z1):
                    if (y[k]-y1)*(x2-x1)*(z2-z1) == (z[k]-z1)*(x2-x1)*(y2-y1):
                        continue
            # 평면의 방정식 ax + by + cz + d = 0
            a = y1*(z2-z[k]) + y2*(z[k]-z1) + y[k]*(z1-z2)
            b = z1*(x2-x[k]) + z2*(x[k]-x1) + z[k]*(x1-x2)
            c = x1*(y2-y[k]) + x2*(y[k]-y1) + x[k]*(y1-y2)
            d = x1*(y2*z[k] - y[k]*z2) + x2*(y[k]*z1 - y1*z[k]) + x[k]*(y1*z2 - y2*z1)
            if a!= 0 and b != 0 and c != 0:
                flag = 1
                break
        if flag == 1:
            for i in range(k+1, n):
                func = a*x[i] + b*y[i] + c*z[i]
                if func != d:
                    ans = 'NIE'
                    break
    print('#%d' %tc, ans)