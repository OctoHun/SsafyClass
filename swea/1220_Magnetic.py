for i in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for j in range(100):
        a = 0
        temp = [0] * 100
        for k in range(100):
            if arr[k][j] != 0:
                temp[a] = arr[k][j]
                a += 1
        for k in range(99):
            if temp[k] + 1 == temp[k+1]:
                cnt += 1
    print('#%d' %i, cnt)