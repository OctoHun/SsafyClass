for _ in range(10):
    case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    sum_d = 0
    sum_cd = 0
    for i in range(100):
        sum_row = 0
        sum_column = 0
        sum_d += arr[i][i]
        sum_cd += arr[i][99-i]
        for j in range(100):
            sum_row += arr[i][j]
            sum_column += arr[j][i]
        if sum_row > ans:
            ans = sum_row
        if sum_column > ans:
            ans = sum_column
    if sum_d > ans:
        ans = sum_d
    if sum_cd > ans:
        ans = sum_cd
    print('#%d' %case, ans)