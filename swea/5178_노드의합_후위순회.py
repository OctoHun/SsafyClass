def sum_node(l):
    a = 0
    b = 0
    if tree[l] == -1:
        if l*2 <= n:
            a = sum_node(l*2)
        if (l*2)+1 <= n:
            b = sum_node((l*2)+1)
        return a+b
    return tree[l]


t = int(input())
for i in range(1, t+1):
    n, m, l = map(int, input().split())
    tree = [-1] * (n + 1)
    for j in range(m):
        c = list(map(int, input().split()))
        tree[c[0]] = c[1]
    ans = sum_node(l)
    print('#%d' %i, ans)