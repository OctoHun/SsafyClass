import sys
n, k = map(int, input().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
money = 0
cnt = 0
for i in range(n-1, -1, -1):
    while arr[i] <= k-money:
        money += arr[i]
        cnt += 1
        if money == k:
            break
    if k == money:
        break
print(cnt)