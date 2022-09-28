n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
cnt_row = 0
cnt_col = 0
for i in range(n):
    flag = 0
    for j in range(m):
        if arr[i][j] == 'X':
            flag = 1
            break
    if flag == 0:
        cnt_row += 1
for i in range(m):
    flag = 0
    for j in range(n):
        if arr[j][i] == 'X':
            flag = 1
            break
    if flag == 0:
        cnt_col += 1
if cnt_row >= cnt_col:
    print(cnt_row)
else:
    print(cnt_col)