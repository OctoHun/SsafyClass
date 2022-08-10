t = int(input())
for i in range(1, t+1):
    day = int(input())
    arr = list(map(int, input().split()))
    while(1):
        for j in range(arr.find(max(arr))):