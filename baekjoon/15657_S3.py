import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in itertools.combinations_with_replacement(arr, m):
    for j in range(m):
        print(i[j], end = ' ')
    print()