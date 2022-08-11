t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for j in range(n):
        cnt_row = 0
        cnt_col = 0
        for l in range(n):
            if arr[j][l] == 1:
                cnt_row += 1
            else:
                cnt_row = 0
            if arr[l][j] == 1:
                cnt_col += 1
            else:
                cnt_col = 0
            if cnt_row == k:
                ans += 1
            elif cnt_row >k:
                ans -= 1
                cnt_row = 0
            if cnt_col == k:
                ans += 1
            elif cnt_col > k:
                ans -= 1
                cnt_col = 0
    print('#%d' %i, ans)