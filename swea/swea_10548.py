t = int(input())
for i in range(1, t+1):
    N = int(input())
    b = list(map(int, input().split()))
    result = 0
    rst_index = 0
    for j in range(N):
        cnt = 0
        for k in range(j+1, N):
            if b[j]<=b[k]:
                cnt += 1
        if N-1-j-cnt > result:
            result = N-1-j-cnt
    print('#%d' %i, result)