from collections import deque
arr = [0]*100000
for i in range(100000):
    arr[i] = list(input())
    if len(arr[i]) == 1 and arr[i][0] == '.':
        break
stack = deque()
for j in range(i):
    ans = 1
    for k in arr[j]:
        if k == '(' or k == '[':
            stack.append(k)
        elif k == ')':
            if not stack:
                ans = 0
                break
            else:
                a = stack.pop()
                if a != '(':
                    ans = 0
                    break
        elif k == ']':
            if not stack:
                ans = 0
                break
            else:
                a = stack.pop()
                if a != '[':
                    ans = 0
                    break
    if stack:
        ans = 0
    if ans == 1:
        print('yes')
    else:
        print('no')
    stack.clear()