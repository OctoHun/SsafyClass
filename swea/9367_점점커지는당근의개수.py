t = int(input())
for i in range(1, t+1):
    n = int(input())
    c = list(map(int, input().split()))
    max = 0
    cnt = 1
    for j in range(len(c)-1):
        if c[j] +1 == c[j+1]:
            cnt += 1
        else:
            cnt = 1
        if cnt > max:
            max = cnt
    print('#%d' %i, max)