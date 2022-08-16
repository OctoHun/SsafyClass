for i in range(1, 11):
    t = int(input())
    arr = [input() for _ in range(100)]
    ans = [0] * 101
    n = 2

    while n < 101:
        n1 = n//2
        for j in range(100):
            for k in range(100-n+1):
                cnt = 0
                for a in range(n1):
                    if arr[j][k+a] == arr[j][k+n-1-a]:
                        cnt += 1
                if cnt == n1:
                    ans[n] += 1
                    break
                cnt = 0
                for a in range(n1):
                    if arr[k+a][j] == arr[k+n-1-a][j]:
                        cnt += 1
                if cnt == n1:
                    ans[n] += 1
                    break
            if cnt == n1:
                break
        n += 1
    for j in range(100, -1, -1):
        if ans[j] == 1:
            result = j
            break
    print('#%d' %i, result)