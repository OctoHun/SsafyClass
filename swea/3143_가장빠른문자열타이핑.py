t = int(input())
for i in range(1, t+1):
    a, b = input().split()
    ans = 0
    cnt = 0
    for j in a:
        cnt += 1
    lengtha = cnt
    cnt = 0
    for j in b:
        cnt += 1
    lengthb = cnt
    j = 0
    while j <= lengtha-lengthb:
        cnt = 0
        for k in range(lengthb):
            if a[j+k] == b[k]:
                cnt += 1
        if cnt == lengthb:
            ans += 1
            j += lengthb
            continue
        j += 1
    ans = lengtha - (lengthb - 1) * ans
    print('#%d' %i, ans)