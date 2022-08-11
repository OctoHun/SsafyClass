t = int(input())
for i in range(1, t+1):
    a = input()
    b = [0] * 101
    case = list(map(int, input().split()))
    for j in case:
        b[j] += 1
    maxindex = 0
    for j in range(1, 101):
        if b[j]>=b[maxindex]:
            maxindex=j
    print('#%d' %i, maxindex)