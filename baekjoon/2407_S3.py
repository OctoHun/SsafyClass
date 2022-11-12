n, m = map(int, input().split())
ans = 1
for i in range(m):
    ans = ans *(n-i)
for i in range(m, 0, -1):
    ans = ans // i
print(ans)