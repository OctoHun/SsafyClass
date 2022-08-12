t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    max = 0
    for j in range(n):
        cnt = 0
        for k in range(m):
            if arr[j][k] == 1:
                cnt += 1
            else:
                cnt = 0
                if m-k-1<=max:
                    break
            if cnt > max:
                max = cnt
    for j in range(m):
        cnt = 0
        for k in range(n):
            if arr[k][j] == 1:
                cnt += 1
            else:
                cnt = 0
                if n-k-1<=max:
                    break
            if cnt > max:
                max = cnt
    print('#%d' %i, max)
