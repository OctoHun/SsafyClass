t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input()))
    max = 0
    cnt = 0
    for j in range(n):
        if arr[j]==1:
            cnt += 1
        else:
            cnt = 0
        if cnt > max:
            max = cnt
    print('#%d' %i, max)