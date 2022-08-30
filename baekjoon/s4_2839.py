def dfs(k, s):
    global n
    if n == 0:
        return
    k = n % 5 + 5
    if k % 3 == 0:






n = int(input())
if n % 5 == 0:
    ans = n//5
else:
    k = n//5
    s = n%5
    def(k, s)