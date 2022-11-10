import heapq
n = int(input())
arr = [64]
heapq.heapify(arr)
while sum(arr) > n:
    stick = heapq.heappop(arr)
    heapq.heappush(arr, stick // 2)
    if sum(arr) >= n:
        pass
    else:
        heapq.heappush(arr, stick // 2)
print(len(arr))
