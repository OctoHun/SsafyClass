for i in range(1, 11):
    n = int(input())
    s = input()
    stack = [0] * n
    top = -1
    result = ""
    for j in range(n):
        if "0" <= s[j] <= "9":
            result += s[j]
        else:
            if top > -1:
                result += stack[top]
                top -= 1
            top += 1
            stack[top] = s[j]
    while top > -1:
        result += stack[top]
        top -= 1

    ans = [0] * n
    ctn = 0
    for j in result:
        if '0' <= j <= '9':
            ans[ctn] = int(j)
            ctn += 1
        elif j == '+':
            ans[ctn-2] = ans[ctn-2] + ans[ctn-1]
            ctn -= 1
    print('#%d' %i, ans[0])