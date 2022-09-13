def tree(n):
    global cnt
    cnt += 1
    if c1[n] != 0:
        tree(c1[n])
        if c2[n] != 0:
            tree(c2[n])
    return


t = int(input())
for j in range(1, t+1):
    e, n = map(int, input().split())
    c1 = [0] * (e + 2)
    c2 = [0] * (e + 2)
    edges = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        if c1[edges[i]] == 0:
            c1[edges[i]] = edges[i+1]
        else:
            c2[edges[i]] = edges[i+1]
    cnt = 0
    tree(n)
    print('#%d' %j, cnt)