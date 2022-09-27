from collections import deque
n = int(input())
arr = [list(input().split()) for _ in range(n)]
q = deque()
for i in range(n):
    if arr[i][0] == 'push_front':
        q.appendleft(arr[i][1])
    elif arr[i][0] == 'push_back':
        q.append(arr[i][1])
    elif arr[i][0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif arr[i][0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(q))
    elif arr[i][0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif arr[i][0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif arr[i][0] == 'back':
        if q:
            print(q[len(q)-1])
        else:
            print(-1)