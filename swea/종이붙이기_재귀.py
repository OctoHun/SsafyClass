def fill(n):
    global cnt
    if n == 0:
        cnt += 1
        return
    elif n < 0:
        return
    for i in [1, 2, 2]:
        fill(n-i)
    return


t = int(input())
for i in range(1, t+1):
    n = int(input())
    cnt = 0
    fill(n//10)
    print('#%d' %i, cnt)

