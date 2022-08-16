global cnt, prime
def prime_arr():
    arr = [True] * 1000
    arr[0] = False
    arr[1] = False
    m = int(1000**0.5)
    for i in range(2, m+1):
        if arr[i]:
            for j in range(2*i, 1000, i):
                arr[j] = False
    return arr


t = int(input())
arr = prime_arr()
a = 0
for i in range(1000):
    if arr[i]:
        a += 1
prime = [0] * a
a = 0
for i in range(2, 1000):
    if arr[i] == True:
        prime[a] = i
        a += 1
for i in range(1, t+1):
    n = int(input())
    cnt = 0
    for j in range(a-2, -1, -1):
        if prime[j] <= n:
            x = prime[j]
            for k in range(j, -1, -1):
                if prime[k] <= n-x:
                    y = prime[k]
                    for l in range(k, -1, -1):
                        if prime[l] == n-x-y:
                            cnt += 1
    print('#%d' %i, cnt)