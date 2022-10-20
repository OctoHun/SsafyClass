import sys
def dfs(now):
    global cnt
    if now == n:
        cnt += 1
        return
    if now > n:
        return
    dfs(now+1)
    dfs(now+2)
    dfs(now+3)


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    cnt = 0
    dfs(0)
    print(cnt)