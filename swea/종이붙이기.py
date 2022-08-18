def fill(n):
    global arr
    if n == 300:
        return
    arr[n] = arr[n-1] + arr[n-2] +arr[n-2]
    fill(n+1)


t = int(input())
arr = [0] * 301
arr[1] = 1
arr[2] = 3
fill(3)
for i in range(1, t+1):
    n = int(input())
    n = n//10
    print('#%d' %i, arr[n])