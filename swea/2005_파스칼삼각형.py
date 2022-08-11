t = int(input())
for i in range(1, t+1):
    n = int(input())
    if n%2 == 0:
        print('#%d' %i, n//2 * -1)
    else:
        print('#%d' %i, n//2+1)