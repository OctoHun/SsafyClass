def arr_prime():
    arr = [True] * (1000001)
    arr[1] = False
    m = int(1000001 ** 0.5)
    for i in range(2, m + 1):
        if arr[i]:
            for j in range(2*i, 1000001, i):
                arr[j] = False
    return arr


t = int(input())
arr = arr_prime()
for i in range(1, t+1):
    d, a, b = map(int, input().split())
    d = str(d)
    cnt = 0
    for j in range(a, b+1):
        if arr[j]:
            if d in str(j):
                cnt += 1
    print('#%d' %i, cnt)