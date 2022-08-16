ans = 1


def func(a, b):
    global ans
    if b == 0:
        return ans
    ans *= a
    result = func(a, b-1)
    return result


for i in range(10):
    t = int(input())
    n, m = map(int, input().split())
    ans = 1
    print('#%d' %t, func(n, m))