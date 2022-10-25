import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum = [0] * n
sum[0] = arr[0]
for i in range(1, n):
    sum[i] = sum[i-1] + arr[i]
for i in range(m):
    arrm = list(map(int, sys.stdin.readline().split()))
    if arrm[0]-2 > -1:
        print(sum[arrm[1]-1]-sum[arrm[0]-2])
    else:
        print(sum[arrm[1]-1])