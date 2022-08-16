for i in range(1, 11):
    n= int(input())
    arr = [input() for _ in range(8)]
    n1 = n//2
    ans = 0
    for j in range(8):
        for k in range(8-n+1):
            cnt = 0
            for a in range(n1):
                if arr[j][k+a] == arr[j][k+n-1-a]:
                    cnt += 1
            if cnt == n1:
                ans += 1
            cnt = 0
            for a in range(n1):
                if arr[k+a][j] == arr[k+n-1-a][j]:
                    cnt += 1
            if cnt == n1:
                ans += 1
    print('#%d' %i, ans)