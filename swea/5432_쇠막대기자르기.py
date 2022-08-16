t = int(input())
for i in range(1, t+1):
    a = input()
    cnt = 0
    ans = 0
    pipe = 0
    for j in a:
        cnt += 1
    length = cnt
    j = 0
    while j < length-1:
        if a[j] == '(' and a[j+1] == ')':
            ans += pipe
            j += 2
            continue
        elif a[j] == '(':
            pipe += 1
            ans += 1
        elif a[j] == ')':
            pipe -= 1
        j += 1
    print('#%d' %i, ans)