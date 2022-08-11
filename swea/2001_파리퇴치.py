t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max = 0
    for j in range(n-m+1):
        for k in range(n-m+1):
            sum = 0
            for a in range(m):
                for b in range(m):
                    sum += arr[j+a][k+b]
            if sum>max:
                max = sum
    print('#%d' %i, max)