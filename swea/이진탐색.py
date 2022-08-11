def search(num, end):
    start = 1
    cnt = 0
    middle = (start+end)//2
    while num != middle:
        if num < middle:
            end = middle
            middle = (start + end) // 2
        else:
            start = middle
            middle = (start + end) // 2
        cnt += 1
    return cnt

t = int(input())
for i in range(1, t+1):
    p, a, b = map(int, input().split())
    arr = [0] * p
    ansa = search(a, p)
    ansb = search(b, p)
    if ansa<ansb:
        print('#%d' %i, 'A')
    elif ansa>ansb:
        print('#%d' % i, 'B')
    else:
        print('#%d' %i, 0)