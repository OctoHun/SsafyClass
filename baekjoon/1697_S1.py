from collections import deque

def bfs():
    while q:
        target, cnt = q.popleft()
        if target == k:
            return cnt
        if target < k:
            if target+1 < 100001 and visited[target+1] == 0:
                visited[target+1] = 1
                q.append((target+1, cnt+1))
            if target*2 < 100001 and visited[target*2] == 0:
                visited[target*2] = 1
                q.append((target*2, cnt+1))
        if target > 0 and visited[target-1] == 0:
            visited[target-1] = 1
            q.append((target-1, cnt+1))


q = deque()
n, k = map(int, input().split())
q.append((n, 0))
visited = [0] * 100001
visited[n] = 1
if n >= k:
    print(n-k)
else:
    ans = bfs()
    print(ans)