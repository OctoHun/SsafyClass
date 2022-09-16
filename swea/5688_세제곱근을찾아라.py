t = int(input())
for tc in range(1, t+1):
    n = int(input())
    a = n**(1/3)
    a = int(a)
    b = [0] * 6
    j = 0
    flag = 0
    for i in range(-3, 3):
        b[j] = i+a
        j += 1
    for i in b:
        if i**3 == n:
            print('#%d' %tc, i)
            flag = 1
            break

    if flag == 0:
        print('#%d' %tc, -1)