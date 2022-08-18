def delete(n, a):
    global b, s
    b = ''
    cnt = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            for j in range(1, n):
                if i-j >= 0 and i+1+j < n-1 and a[i-j] == a[i+1+j]:
                    cnt = j
                else:
                    break
            if i-cnt > 0:
                b += a[:i-cnt]
            if i+1+cnt < n-1:
                b += a[i+2+cnt:]
            s = b
            delete(len(b), b)
            break
    return


for i in range(1, 11):
    n, s = input().split()
    n = int(n)
    b = ''
    delete(n, s)
    print('#%d' %i, s)