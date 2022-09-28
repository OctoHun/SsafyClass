# from collections import deque
#
# def bfs():
#     q = deque()
#     q.append([n, 0])
#     visited = [0] * 1000001
#     visited[n] = 1
#     while 1:
#         a, cnt = q.popleft()
#         if a == m:
#             return cnt
#         if a + 1 <= 1000000 and visited[a + 1] == 0 and a < m:
#             visited[a + 1] = 1
#             q.append([a+1, cnt+1])
#         if a * 2 <= 1000000 and visited[a * 2] == 0 and a < m:
#             visited[a * 2] = 1
#             q.append([a*2, cnt+1])
#         if a-1 > 0 and visited[a - 1] == 0:
#             visited[a - 1] = 1
#             q.append([a-1, cnt+1])
#         if a-10 > 0 and visited[a - 10] == 0:
#             visited[a - 10] = 1
#             q.append([a-10, cnt+1])
#
#
# t = int(input())
# for tc in range(1, t+1):
#     n, m = map(int, input().split())
#     print('#%d' %tc, bfs())



def bfs():
    q = [0] * 1000000
    q[0] = [n, 0]
    visited = [0] * 1000001
    visited[n] = 1
    now = 0
    index = 0
    while 1:
        a, cnt = q[now]
        if a == m:
            return q[now][1]
        if a + 1 <= 1000000 and visited[a + 1] == 0 and a < m:
            visited[a + 1] = 1
            index+=1
            q[index] = [a+1, cnt+1]
        if a * 2 <= 1000000 and visited[a * 2] == 0 and a < m:
            visited[a * 2] = 1
            index+=1
            q[index] = [a*2, cnt+1]
        if visited[a - 1] == 0 and a-1 > 0:
            visited[a - 1] = 1
            index+=1
            q[index] = [a-1, cnt+1]
        if visited[a - 10] == 0 and a-10 > 0:
            visited[a - 10] = 1
            index+=1
            q[index] = [a-10, cnt+1]
        now += 1


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    ans = bfs()
    print('#%d' %tc, ans)