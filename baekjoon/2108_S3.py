import sys

N = int(sys.stdin.readline())
arr = [0] * N
for i in range(N):
    a = int(sys.stdin.readline())
    arr[i] = a
average = round(sum(arr)/N)
arr.sort()
middle = arr[N//2]
num_range = arr[N-1] - arr[0]
cnt = 0
max = 0
many = dict()
first = 9998
second = 9999
for i in range(N):
    if arr[i] in many:
        many[arr[i]] = many[arr[i]] + 1
    else:
        many[arr[i]] = 1
for result, time in many.items():
    if time > max:
        max = time
        first = result
        second = 9999
    elif time == max:
        if result < first:
            second = first
            first = result
        elif result < second:
            second = result
print(average)
print(middle)
if second == 9999:
    print(first)
else:
    print(second)
print(num_range)