t = int(input())
for i in range(1, t+1):
    tc, n = map(str, input().split())
    print(tc)
    n = int(n)
    index = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    arr = input().split()
    for j in range(n):
        for k in range(10):
            if arr[j] == index[k]:
                arr[j] = k
                break
    for j in range(n):
        for k in range(j+1, n):
            if arr[j]>arr[k]:
                arr[j], arr[k] = arr[k], arr[j]
    for j in range(n):
        for k in range(10):
            if arr[j] == k:
                arr[j] = index[k]
                break
    for j in range(n):
        print(arr[j], end = ' ')
    print()