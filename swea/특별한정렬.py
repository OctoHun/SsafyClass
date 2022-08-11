t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print('#%d' %i, end = ' ')
    for j in range(n):
        for k in range(j+1, n):
            if arr[j]>arr[k]:
                arr[j], arr[k] = arr[k], arr[j]
    for j in range(5):
        print(arr[n-1-j], end = ' ')
        print(arr[j], end = ' ')
    print()