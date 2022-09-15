t = int(input())
for i in range(1, t+1):
    n, a, b = map(int, input().split())
    min = 100000000
    for j in range(1, n):
        for k in range(1, n):
            if j * k > n:
                break
            result = a * abs(j-k) + b * (n - j * k)
            if result >= 0 and result < min:
                min = result
    print('#%d' %i, min)