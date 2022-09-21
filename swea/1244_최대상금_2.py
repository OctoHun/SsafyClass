def change(i, now):
    global max, maxnum
    if i == n:
        result = ''
        for j in range(length):
            result += a[j]
        if int(result) > max:
            max = int(result)
        return
    elif maxnum == max:
        if flag == 0:
            if (n-i)%2 == 1:
                a[length-1], a[length-2] = a[length-2], a[length-1]
                result = ''
                for j in range(length):
                    result += a[j]
                max = int(result)
                maxnum = max
            return
    for j in range(now, length):
        for k in range(j+1, length):
            if a[j] <= a[k]:
                a[j], a[k] = a[k], a[j]
                change(i+1, j)
                a[j], a[k] = a[k], a[j]
            if max == maxnum:
                return


t = int(input())
for tc in range(1, t+1):
    a, n = input().split()
    n = int(n)
    max = int(a)
    length = len(a)
    flag = 0
    a = list(a)
    temp = [0] * length
    maxnum = ''
    for i in range(length):
        temp[i] = a[i]
    for i in range(length):
        for j in range(i+1, length):
            if temp[i] < temp[j]:
                temp[i], temp[j] = temp[j], temp[i]
            if temp[i] == temp[j]:
                flag = 1
    for i in range(length):
        maxnum += temp[i]
    maxnum = int(maxnum)
    change(0, 0)
    print('#%d' %tc, max)