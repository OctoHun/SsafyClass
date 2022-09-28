n, k = map(int, input().split())
ans = 1
for i in range(k):
    ans = ans * (n-i)
for i in range(k, 0, -1):
    ans = ans // i
print(ans)