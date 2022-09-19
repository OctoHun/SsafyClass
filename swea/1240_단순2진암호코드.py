t = int(input())
num = [0] * 62
arr = [13, 25, 19, 61, 35, 49, 47, 59, 55, 11]
for i in range(10):
    num[arr[i]] = i
for tc in range(1, t+1):
    n, m = map(int, input().split())
    pwd = [input() for _ in range(n)]
    row = 0
    col = 0
    odd, even = 0, 0
    for i in range(n):
        for j in range(m-1, -1, -1):
            if pwd[i][j] == '1':
                row = i
                col = j
                break
        if col != 0:
            break
    for i in range(col-55, col, 14):
        temp = ''
        for j in range(7):
            temp += pwd[row][i+j]
        odd += num[int(temp, 2)]
        temp = ''
        for j in range(7):
            temp += pwd[row][i+7+j]
        even += num[int(temp, 2)]

    ans = (odd*3) + even
    if ans % 10 == 0:
        print('#%d' %tc, even+odd)
    else:
        print('#%d' %tc, 0)