import sys
import heapq
n = int(sys.stdin.readline())
arr = []
heapq.heapify(arr)
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if arr:
            result = heapq.heappop(arr)
            print(-result)
        else:
            print(0)
    else:
        heapq.heappush(arr, -a)