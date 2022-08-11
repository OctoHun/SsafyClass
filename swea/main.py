t = int(input())
for i in range(1, t+1):
    K, N, M = map(int, input().split())
    a = list(map(int, input().split()))
    bus = 0
    cnt=0
    result = 1
    for j in range(M-1):
        if a[0]>K or N-a[len(a)-1]>K or a[j+1]-a[j]>K:
            result = 0
            break
    if result == 1:
        while(1):
            bus += K
            if bus >= N:
                break
            for l in range(M-1, -1, -1):
                if bus >= a[l]:
                    cnt+=1
                    bus = a[l]
                    break
    print('#%d' %i, cnt)