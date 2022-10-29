import sys
import heapq
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
q = []
heapq.heapify(q)
for i in range(n):
    if arr[i] == 0:
        if q:
            result = heapq.heappop(q)
            print(result)
        else:
            print(0)
    else:
        heapq.heappush(q, arr[i])