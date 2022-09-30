def select(x, cnt):
    global max, min
    if cnt == n:
        if x > max:
            max = x
        if x < min:
            min = x
        return
    for j in range(4):
        if temp[j] > 0:
            temp[j] -= 1
            if j == 0:
                new = x+num[cnt]
            elif j == 1:
                new = x-num[cnt]
            elif j == 2:
                new = x*num[cnt]
            else:
                new = int(x/num[cnt])
            select(new, cnt+1)
            temp[j] += 1


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    temp = list(map(int, input().split()))
    num = list(map(int, input().split()))
    cnt = 0
    max = -100000001
    min = 100000001
    select(num[0], 1)
    print('#%d' %tc, max-min)