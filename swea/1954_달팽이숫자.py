t = int(input())
for i in range(1, t+1):
    a = int(input())
    arr = [[0]*a for _ in range(a)]
    num = 1
    row_start=0
    col_start=-1
    col_end = a
    row_end = a
    while(num <= a*a):
        for j in range(col_start+1, col_end):
            arr[row_start][j] = num
            num += 1
        col_end -= 1
        for j in range(row_start+1, row_end):
            arr[j][col_end] = num
            num += 1
        row_end -= 1
        for j in range(col_end-1, col_start, -1):
            arr[row_end][j] = num
            num += 1
        col_start += 1
        for j in range(row_end-1, row_start, -1):
            arr[j][col_start] = num
            num += 1
        row_start += 1
    print('#%d' %i)
    for j in range(a):
        for k in range(a):
            print(arr[j][k], end = ' ')
        print()


