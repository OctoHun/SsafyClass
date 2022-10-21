t = int(input())
for tc in range(t):
    n = int(input())
    arr = dict()
    for i in range(n):
        a = list(input().split())
        if a[1] in arr:
            arr[a[1]] += 1
        else:
            arr[a[1]] = 1
    ans = 1
    for i in arr.values():
        ans = ans * (i+1)
    print(ans-1)