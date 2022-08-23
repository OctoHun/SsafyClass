def select(row, sum, visited):
    global min, arr, n
    if row == n:
        if min > sum:
            min = sum
        return
    elif min < sum:
        return
    for j in range(n):
        if visited[j] == 0:
            visited[j] = 1
            select(row+1, sum + arr[row][j], visited)
            visited[j] = 0
    return


t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min = 1000
    visited = [0] * n
    select(0, 0, visited)
    print('#%d' %i, min)