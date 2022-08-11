global a
a = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def cnt(x, n, k, b):
    global a
    if x == n and k == 0:
        a += 1
        return 0
    elif k == 0:
        return 0
    for i in range(b, -1, -1):
        if arr[i] <= k:
            cnt(x + 1, n, k - arr[i], i-1)
    return a

t = int(input())
for i in range(1, t + 1):
    a = 0
    n, k = map(int, input().split())
    ans = cnt(0, n, k, 11)
    print('#%d' % i, ans)
