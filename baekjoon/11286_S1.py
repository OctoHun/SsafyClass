import sys
import heapq

n = int(sys.stdin.readline())
plusq = []
minusq = []
heapq.heapify(plusq)
heapq.heapify(minusq)
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if minusq:
            if plusq:
                if plusq[0] >= minusq[0][0]:
                    target = heapq.heappop(minusq)
                    print(target[1])
                else:
                    target = heapq.heappop(plusq)
                    print(target)
            else:
                target = heapq.heappop(minusq)
                print(target[1])
        elif plusq:
            target = heapq.heappop(plusq)
            print(target)
        else:
            print(0)
    elif a < 0:
        heapq.heappush(minusq, (-a, a))
    elif a > 0:
        heapq.heappush(plusq, a)