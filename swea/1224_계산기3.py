for i in range(1, 11):
    n = int(input())
    d = {'+' : 1, '*' : 2, "(" : 0}
    s = input()
    stack = [0] * n
    top = -1
    result = ""
    for j in range(n):
        if "0" <= s[j] <= "9":
            result += s[j]
        elif s[j] == "(":
            top += 1
            stack[top] = s[j]
        elif s[j] == ")":
            for k in range(top, -1, -1):
                if stack[top] == "(":
                    stack[top] = 0
                    top -= 1
                    break
                result += stack[top]
                top -= 1
        else:
            if top > -1 and d[s[j]] <= d[stack[top]]:
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
        elif j == '*':
            ans[ctn-2] = ans[ctn-2] * ans[ctn-1]
            ctn -= 1
    print('#%d' %i, ans[0])