t = int(input())
for i in range(1, t+1):
    a = list(map(int, input().split()))
    sum = 0
    for j in range(0, 10):
        if a[0]>a[j]:
            a[0], a[j] = a[j], a[0]
        if a[9]<a[9-j]:
            a[9], a[9-j] = a[9-j], a[9]
    for j in range(1, 9):
        sum += a[j]
    print('#%d' %i, round(sum/8))