t = int(input())
for i in range(1, t+1):
    day = int(input())
    arr = list(map(int, input().split()))
    now = 0
    max_index = -1
    sum = 0
    temp = 0
    while max_index != day-1:
        max = 0
        for j in range(max_index+1, day):
            if arr[j] > max:
                max = arr[j]
                max_index = j
        for j in range(temp, max_index):
            sum += arr[max_index]-arr[j]
        temp = max_index+1
    print('#%d' %i, sum)