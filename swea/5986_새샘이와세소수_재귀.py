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


def findcase(x, n, a):
    global cnt, prime
    if x == 3 and n == 0:
        cnt += 1
        return 0
    elif x > 3:
        return 0
    for i in range(a, -1, -1):
        if n >= prime[i]:
            findcase(x+1, n-prime[i], i)
    return cnt



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
    cnt = 0
    n = int(input())
    ans = findcase(0, n, len(prime)-1)
    print('#%d' %i, ans)