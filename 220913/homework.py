def tree(n):
    if c1[n]:
        tree(c1[n])
    print(num[n], end = '')
    if c2[n]:
        tree(c2[n])


for t in range(1, 11):
    n = int(input())
    num = [0] * (n+1)
    c1 = [0] * (n+1)
    c2 = [0] * (n+2)
    for i in range(n):
        cnt = 0
        a = list(input().split())
        for j in a:
            cnt += 1
        if cnt == 2:
            num[int(a[0])] = a[1]
        elif cnt == 3:
            num[int(a[0])] = a[1]
            c1[int(a[0])] = int(a[2])
        else:
            num[int(a[0])] = a[1]
            c1[int(a[0])] = int(a[2])
            c2[int(a[0])] = int(a[3])
    print('#%d' %t, end = ' ')
    tree(1)
    print()