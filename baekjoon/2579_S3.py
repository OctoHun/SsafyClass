import sys
def dfs(x):
    if x >= n:
        return
    result[x] = max(result[x-2]+arr[x], result[x-3]+arr[x]+arr[x-1])
    dfs(x+1)


n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
else:
    result = [0]*n
    result[0] = arr[0]
    result[1] = arr[0]+arr[1]
    result[2] = max(arr[0]+arr[2], arr[1]+arr[2])
    dfs(3)
    print(result[n-1])