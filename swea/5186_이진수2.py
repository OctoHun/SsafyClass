t = int(input())
for tc in range(1, t+1):
    n = float(input())
    arr = [-1] * 14
    for i in range(1, 14):
        if n == 0:
            break
        if n >= 2**(-i):
            arr[i] = 1
            n -= 2**(-i)
        else:
            arr[i] = 0
    if arr[13] != -1:
        print('#%d' %tc, 'overflow')
    else:
        print('#%d' %tc, end = ' ')
        for i in range(1, 14):
            if arr[i] != -1:
                print(arr[i], end = '')
        print()