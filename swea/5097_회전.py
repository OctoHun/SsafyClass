t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#%d' %i, arr[m%n])