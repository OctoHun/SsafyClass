t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    temp = [0] * n
    total = [0] * n
    ans = 1
    for j in range(n):
        temp[j] = arr[j][0] * 35 + arr[j][1] * 45 + arr[j][2] * 20
    for j in range(n):
        if temp[k-1]<temp[j]:
            ans += 1
    if ans < (n//10)+1:
        print('#%d' %i, 'A+')
    elif ans < (n//10)*2+1:
        print('#%d' %i, 'A0')
    elif ans < (n//10)*3+1:
        print('#%d' %i, 'A-')
    elif ans < (n//10)*4+1:
        print('#%d' %i, 'B+')
    elif ans < (n//10)*5+1:
        print('#%d' %i, 'B0')
    elif ans < (n//10)*6+1:
        print('#%d' %i, 'B-')
    elif ans < (n//10)*7+1:
        print('#%d' %i, 'C+')
    elif ans < (n//10)*8+1:
        print('#%d' %i, 'C0')
    elif ans < (n//10)*9+1:
        print('#%d' %i, 'C-')
    else:
        print('#%d' %i, 'D0')