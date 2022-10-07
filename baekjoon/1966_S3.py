t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = [0] * n
    now = 0
    max_now = 0
    a = list(map(int, input().split()))
    for i in range(n):
        arr[i] = a[i]
    a.sort(reverse=True)
    now = 0
    while 1:
        if arr[now] == a[max_now]:
            if now == m:
                break
            now += 1
            max_now += 1
        else:
            now += 1
        if now == n:
            now = 0
    print(max_now+1)


