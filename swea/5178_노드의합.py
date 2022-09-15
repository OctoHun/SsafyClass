def sum_node(l):
    if l*2 <= n and (l*2)+1 <= n and tree[l] == -1:
        return sum_node(l*2) + sum_node((l*2)+1)
    elif l*2 <= n and tree[l] == -1:
        return sum_node(l*2)
    return tree[l]


t = int(input())
for i in range(1, t+1):
    n, m, l = map(int, input().split())
    tree = [-1] * (n + 1)
    for j in range(m):
        a = list(map(int, input().split()))
        tree[a[0]] = a[1]
    ans = sum_node(l)
    print('#%d' %i, ans)