t = int(input())
ans = [0] * t
for tc in range(t):
    h, w, n = map(int, input().split())
    x = n//h+1
    y = n%h
    if y == 0:
        y = h
    if x < 10:
        x = '0' + str(x)
    ans[tc] = str(y)+x
for i in range(t):
    print(ans[i])