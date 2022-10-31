import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    arr[i] = [i, arr[i], 0]
arr.sort(key=lambda x:x[1])
for i in range(1, n):
    if arr[i][1] > arr[i-1][1]:
        arr[i][2] = arr[i-1][2] + 1
    else:
        arr[i][2] = arr[i - 1][2]
arr.sort(key=lambda x:x[0])
for i in range(n):
    print(arr[i][2], end = ' ')