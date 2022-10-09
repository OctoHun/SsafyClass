import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort(reverse=True)
sum = 0
flag = 0
h = 0
if n == 1:
    print(tree[0]-m)
else:
    for i in range(n-1):
        sum += (tree[i]-tree[i+1]) * (i+1)
        h = tree[i+1]
        if sum >= m:
            flag = 1
            break
    else:
        for j in range(2000000000):
            sum += n
            h -= 1
            if sum >= m:
                print(h)
                break
    if flag:
        for j in range(2000000000):
            sum -= (i+1)
            h += 1
            if sum < m:
                print(h-1)
                break