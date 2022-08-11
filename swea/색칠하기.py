t = int(input())
for i in range(1, t+1):
    num = int(input())
    arr = [[1]*10 for _ in range(10)]
    cnt = 0
    for j in range(num):
        a = list(map(int, input().split()))
        if a[4] == 1:
            for k in range(a[3]-a[1]+1):
                for l in range(a[2]-a[0]+1):
                    arr[a[1]+k][a[0]+l] *= 2
        if a[4] == 2:
            for k in range(a[3]-a[1]+1):
                for l in range(a[2]-a[0]+1):
                    arr[a[1]+k][a[0]+l] *= 3
    for j in range(10):
        for k in range(10):
            if arr[j][k] % 2 == 0 and arr[j][k] % 3 == 0:
                cnt += 1
    print('#%d' %i, cnt)