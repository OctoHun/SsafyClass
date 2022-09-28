n = int(input())
num = list(map(int, input().split()))
arr = [1]*1001
arr[0], arr[1] = 0, 0

for i in range(1001):
    a = i
    if arr[i] == 1:
        for j in range(a*2, 1001, a):
            if j % a == 0:
                arr[j] = 0
cnt = 0
for i in range(n):
    if arr[num[i]] == 1:
        cnt += 1
print(cnt)