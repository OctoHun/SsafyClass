for i in range(1, 11):
    t = int(input())
    q = list(map(int, input().split()))
    flag = 0
    while flag == 0:
        for j in range(1, 6):
            a = q.pop(0)
            q.append(a-j)
            if q[7] <= 0:
                q[7] = 0
                flag = 1
                break
    print('#%d' %i, end = ' ')
    for j in q:
        print(j, end = ' ')
    print()