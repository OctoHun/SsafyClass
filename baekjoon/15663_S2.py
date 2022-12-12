import sys
import itertools

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
result = itertools.permutations(arr, m)
result = set(result)
result = list(result)
result.sort()
for i in result:
    for j in range(m):
        print(i[j], end = ' ')
    print()
