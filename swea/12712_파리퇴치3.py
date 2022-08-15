t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max = 0
    m1 = m-1
    for j in range(n):
        for k in range(n):
            cnt = 0
            for a in range(k-m1, k+m1+1):
                if 0 <= a < n:
                    cnt += arr[j][a]
            for a in range(j-m1, j+m1+1):
                if 0 <= a < n:
                    cnt += arr[a][k]
            cnt -= arr[j][k]
            if cnt > max:
                max = cnt
            cnt = 0
            for a in range(1, m1+1):
                if j+a < n and k+a < n:
                    cnt += arr[j+a][k+a]
                if j-a >= 0 and k-a >= 0:
                    cnt += arr[j-a][k-a]
                if j-a >= 0 and k+a < n:
                    cnt += arr[j-a][k+a]
                if j+a < n and k-a >= 0:
                    cnt += arr[j+a][k-a]
            cnt += arr[j][k]
            if cnt > max:
                max = cnt
    print('#%d' %i, max)