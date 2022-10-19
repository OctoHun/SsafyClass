t = int(input())
arr = [0] * 41
arr[0] = [1, 0]
arr[1] = [0, 1]
arr[2] = [1, 1]
for i in range(3, 41):
    arr[i] = [arr[i-1][0]+arr[i-2][0], arr[i-1][1]+arr[i-2][1]]
for tc in range(t):
    n = int(input())
    print(arr[n][0], arr[n][1])