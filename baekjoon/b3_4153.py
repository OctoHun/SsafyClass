a = 1
ans = [-1]*10000
cnt = 0
while a != 0:
    a, b, c = map(int, input().split())
    if a >b and a>c:
        if a**2 == b**2 + c**2:
            ans[cnt] = 1
        else:
            ans[cnt] = 0
    elif b >a and b >c:
        if b**2 == a**2 + c**2:
            ans[cnt] = 1
        else:
            ans[cnt] = 0
    else:
        if c**2 == a**2 + b**2:
            ans[cnt] = 1
        else:
            ans[cnt] = 0
    cnt += 1
for i in range(cnt-1):
    if ans[i]:
        print('right')
    else:
        print('wrong')