n, k = map(int, input().split())
arr = [1] * (n+1)
arr[0] = 0
now = 0
j = 0
print('<', end = '')
for i in range(1, n):
    now = 0
    while 1:
        if arr[j] == 1:
            now += 1
        if now == k:
            arr[j] = 0
            print(str(j)+',', end = ' ')
            break
        j += 1
        if j == n+1:
            j = 0
for i in range(n+1):
    if arr[i] == 1:
        print(i, end = '')
print('>')
