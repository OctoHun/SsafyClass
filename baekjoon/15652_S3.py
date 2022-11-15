import itertools

n,m = map(int, input().split())
arr = itertools.combinations_with_replacement(range(1, n+1), m)
for i in arr:
    for j in range(m):
        print(i[j], end=' ')
    print()