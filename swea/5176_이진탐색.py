def node(a):
    global cnt
    if a*2 <= n:
        node(a*2)
    tree[a] = cnt
    cnt += 1
    if (a*2)+1 <= n:
        node((a*2)+1)


t = int(input())
for i in range(1, t+1):
    n = int(input())
    tree = [0] * (n + 1)
    cnt = 1
    node(1)
    print('#%d' %i, tree[1], tree[n//2])