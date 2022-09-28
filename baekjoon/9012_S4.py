t = int(input())
ans = [-1] * t
for tc in range(t):
    s = input()
    stack = [0] * 50
    now = 0
    flag = 0
    for i in s:
        if i == '(':
            stack[now] = '('
            now += 1
        else:
            if now == 0:
                ans[tc] = 0
                break
            else:
                now -= 1
                stack[now] = 0
    if ans[tc] == -1 and stack[0] != 0:
        ans[tc] = 0
    elif ans[tc] == -1:
        ans[tc] = 1
for i in range(t):
    if ans[i] == 1:
        print('YES')
    elif ans[i] == 0:
        print('NO')
    else:
        break