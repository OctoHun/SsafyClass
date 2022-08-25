t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    q = [0] * n
    index = n
    cnt = 0
    for j in range(n):
        q[j] = (j+1, arr[j])
    while q:
        x, y = q.pop(0)
        if y//2 == 0:
            ans = x
            if index < m:
                q.append((index+1, arr[index]))
                index += 1
        else:
            q.append((x, y//2))
    print('#%d' %i, ans)