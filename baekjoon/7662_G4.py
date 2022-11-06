import heapq
import sys
from collections import deque

t = int(sys.stdin.readline())
for tc in range(t):
    maxheap = []
    minheap = []
    visited = deque()
    max_ans = 0
    min_ans = 0
    flag = 0
    heapq.heapify(maxheap)
    heapq.heapify(minheap)
    k = int(sys.stdin.readline())
    id = 0
    for i in range(k):
        a = list(sys.stdin.readline().split())
        if a[0] == 'I':
            visited.append(1)
            heapq.heappush(minheap, (int(a[1]), id))
            heapq.heappush(maxheap, (-int(a[1]), id))
            id += 1
        elif a[0] == 'D':
            flag = 0
            if a[1] == '-1' and minheap:
                while minheap:
                    target, targetid = heapq.heappop(minheap)
                    if visited[targetid] == 1:
                        visited[targetid] = 0
                        break
            elif a[1] == '1' and maxheap:
                while maxheap:
                    target, targetid = heapq.heappop(maxheap)
                    if visited[targetid] == 1:
                        visited[targetid] = 0
                        break
    while maxheap:
        target, targetid = heapq.heappop(maxheap)
        if visited[targetid] == 1:
            max_ans = -target
            flag = 1
            break
    while minheap:
        target, targetid = heapq.heappop(minheap)
        if visited[targetid] == 1:
            min_ans = target
            break
    if flag:
        print(max_ans, min_ans)
    else:
        print('EMPTY')