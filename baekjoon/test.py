def dfs(cnt):
    if cnt >= n:
        return
    result[cnt][0] = arr[cnt][0] + max(result[cnt-1][1], result[cnt-2][1])
    result[cnt][1] = arr[cnt][1] + max(result[cnt-1][0], result[cnt-2][0])
    dfs(cnt+1)



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
if n == 1:
    print(max(arr[0][0], arr[0][1]))
elif n == 2:
    print(max(arr[0][0]+arr[1][1], arr[0][1]+arr[1][0]))
else:
    result = [[0]*2 for _ in range(n)]
    result[0][0] = arr[0][0]
    result[0][1] = arr[0][1]
    result[1][0] = arr[0][1] + arr[1][0]
    result[1][1] = arr[0][0] + arr[1][1]
    dfs(2)
    print(max(result[n-1][0], result[n-1][1]))

