t = int(input())
for i in range(1, t+1):
    s = list(map(str, input().split()))
    length = 0
    for j in s:
        length += 1
    k = 0
    ans = [0] * 1000
    for j in range(length-1):
        if '0' <= s[j] <= '9':
            ans[k] = s[j]
            k += 1
        elif k < 2:
            ans[0] = 'error'
            break
        else:
            if s[j] == '+':
                ans[k-2] = int(ans[k-2]) + int(ans[k-1])
                ans[k-1] = 0
                k -= 1
            elif s[j] == '*':
                ans[k-2] = int(ans[k-2]) * int(ans[k-1])
                ans[k-1] = 0
                k -= 1
            elif s[j] == '/':
                ans[k-2] = int(ans[k-2]) // int(ans[k-1])
                ans[k-1] = 0
                k -= 1
            elif s[j] == '-':
                ans[k-2] = int(ans[k-2]) - int(ans[k-1])
                ans[k-1] = 0
                k -= 1
    for j in range(999):
        if ans[j+1] != 0:
            ans[0] = 'error'
            break
    print('#%d' %i, ans[0])