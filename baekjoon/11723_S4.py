import sys
x = [0]*21
M = int(input())
for i in range(M):
    a = list(sys.stdin.readline().split())
    if a[0] == 'add':
        x[int(a[1])] = 1
    elif a[0] == 'remove':
        x[int(a[1])] = 0
    elif a[0] == 'check':
        if x[int(a[1])]:
            print(1)
        else:
            print(0)
    elif a[0] == 'toggle':
        x[int(a[1])] = not x[int(a[1])]
    elif a[0] == 'all':
        x = [1] * 21
    elif a[0] == 'empty':
        x = [0] * 21