n = int(input())
arr = [0]*1000001
arr[2] = 1
arr[3] = 1
for i in range(4, 1000001):
    arr[i] = arr[i-1]+1
    if i%2 == 0:
        result = arr[i//2]+1
        arr[i] = min(result, arr[i])
    if i%3 == 0:
        result = arr[i//3]+1
        arr[i] = min(arr[i], result)
print(arr[n])