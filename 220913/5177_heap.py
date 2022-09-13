def enq(n):
    global last
    last += 1
    heap[last] = n

    #만약 새로 추가된 원소가 부모 노드보다 더 커버린 경우 자리 바꾼다
    c = last    # 새로 추가된 노드(자식노드)
    p = c // 2  # 부모 노드
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    last = 0
    heap = [0] * (n+1)
    ans = 0
    for j in arr:
        enq(j)
    while n > 0:
        n = n//2
        ans += heap[n]
    print('#%d' %i, ans)