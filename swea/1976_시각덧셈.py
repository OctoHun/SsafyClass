t = int(input())
for i in range(1, t+1):
    a = list(map(int, input().split()))
    hour = a[0]+a[2]
    min = a[1]+a[3]
    if min>=60:
        min -= 60
        hour += 1
    if hour > 12:
        hour -= 12
    print('#%d' %i, hour, min)