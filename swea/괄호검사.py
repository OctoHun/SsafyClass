t = int(input())
for i in range(1, t+1):
    n = input()
    arr = [0] * 100
    a = 0
    ans = 1
    for j in n:
        if j == '(':
            arr[a] += 1
            a += 1
        elif j == '{':
            arr[a] += 2
            a += 1
        elif j == ')':
            if a-1 < 0 or arr[a-1] != 1:
                ans = 0
                break
            arr[a-1] -= 1
            a -= 1
        elif j == '}':
            if a-1 < 0 or arr[a-1] != 2:
                ans = 0
                break
            arr[a-1] -= 2
            a -= 1
    if arr[0] != 0:
        ans = 0
    print('#%d' %i, ans)