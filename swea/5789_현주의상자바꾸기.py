t = int(input())
for i in range(1, t+1):
    n, q = map(int, input().split())
    box = [0] * n
    l = [0] * 1000
    r = [0] * 1000
    for j in range(q):
        l[j], r[j] = map(int, input().split())
        for k in range(l[j], r[j]+1):
            box[k-1] = j+1
    print('#%d' %i, end = ' ')
    for j in range(n):
        print(box[j], end = ' ')
    print()