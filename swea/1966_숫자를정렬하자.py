t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    for j in range(n):
        for k in range(j+1, n):
            if arr[j]>arr[k]:
                arr[j], arr[k] = arr[k], arr[j]
    print('#%d' %i, end = ' ')
    for j in range(n):
        print(arr[j], end = ' ')
    print()