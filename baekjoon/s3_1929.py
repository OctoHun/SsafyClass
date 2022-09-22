m, n = map(int, input().split())
arr = [1] * 1000001
arr[0], arr[1] = 0, 0
for i in range(1000001):
    if arr[i] == 1:
        for j in range(i*2, 1000001, i):
            arr[j] = 0
for i in range(m, n+1):
    if arr[i] == 1:
        print(i)