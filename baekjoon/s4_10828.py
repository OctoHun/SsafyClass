n = int(input())
stack = []
arr = [list(input().split()) for _ in range(n)]
for i in range(n):
    if arr[i][0] == 'push':
        stack.append(arr[i][1])
    elif arr[i][0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(stack))
    elif arr[i][0] == 'empty':
        if stack:
            print(1)
        else:
            print(0)
    elif arr[i][0] == 'top':
        if stack:
            print(stack(len(stack)-1))
        else:
            print(-1)