#문자열 method 쓰지 말고 풀어보기

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
    for j in range(n):
        for k in range(n):
            if arr[j]>arr[k]:
                arr[j], arr[k] = arr[k], arr[j]
    for j in range(n):
        for k in range(10):
            if arr[j] == k:
                arr[j] = arr[k]
    for j in range(n):
        print(arr[j], end = ' ')
