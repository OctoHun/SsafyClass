t = int(input())
for i in range(1, 1+t):
    N = int(input())
    a=b=c=d=e=0
    for j in range(1000000):
        if N % 2 == 0:
            N = N // 2
            a += 1
        elif N % 3 == 0:
            N = N//3
            b += 1
        elif N % 5 == 0:
            N = N//5
            c += 1
        elif N % 7 == 0:
            N = N//7
            d += 1
        elif N % 11 == 0:
            N = N // 11
            e += 1
    print('#%d' %i, a, b, c, d, e)