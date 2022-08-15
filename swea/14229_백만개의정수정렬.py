import sys
sys.stdin = open("input.txt", "r")
A = list(map(int, input().split()))
arr = [0] * 1000001
for i in A:
    arr[i] += 1
for i in range(1000000):
    arr[i+1] += arr[i]
    if arr[i+1] >= 500001:
        print(i+1)
        break