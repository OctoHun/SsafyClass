t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    m1 = m//2
    ans = ''
    for j in range(n):
        for k in range(n):
            if n-m >= k:
                cnt = 0
                for l in range(m1):
                    if arr[j][k+l] == arr[j][k+m-1-l]:
                        cnt += 1
                    else:
                        break
                if cnt == m1:
                    for l in range(m):
                        ans += arr[j][k+l]
            if n-m >= j:
                cnt = 0
                for l in range(m1):
                    if arr[j+l][k] == arr[j+m-1-l][k]:
                        cnt += 1
                    else:
                        break
                if cnt == m1:
                    for l in range(m):
                        ans += arr[j+l][k]
    print('#%d' %i, ans)
