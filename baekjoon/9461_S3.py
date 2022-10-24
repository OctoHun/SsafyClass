t = int(input())
arr = [0] * 101
arr[1] = 1
arr[2] = 1
arr[3] = 1
for i in range(4, 101):
    arr[i] = arr[i - 3] + arr[i - 2]
for tc in range(t):
    n = int(input())
    print(arr[n])