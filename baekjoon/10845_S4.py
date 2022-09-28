n = int(input())
que = []
arr = [list(input().split()) for _ in range(n)]
for i in range(n):
    if arr[i][0] == 'push':
        que.append(int(arr[i][1]))
    elif arr[i][0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0))
    elif arr[i][0] == 'size':
        print(len(que))
    elif arr[i][0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif arr[i][0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[len(que)-1])
        else:
            print(-1)