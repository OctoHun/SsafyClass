from collections import deque
k = int(input())
arr = deque()
for i in range(k):
    a = int(input())
    if a == 0:
        arr.pop()
    else:
        arr.append(a)
ans = sum(arr)
print(ans)