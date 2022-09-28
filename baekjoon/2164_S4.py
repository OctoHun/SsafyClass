from collections import deque
n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = i+1
q = deque(arr)
while len(q) > 1:
    q.popleft()
    q.rotate(-1)
print(q[0])