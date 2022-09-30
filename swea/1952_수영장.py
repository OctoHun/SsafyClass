def change(x, now):
    global min
    for i in range(now, 10):
        if fee[i]+fee[i+1]+fee[i+2] > month_3:
            change(x-fee[i]-fee[i+1]-fee[i+2]+month_3, i+3)
    if x < min:
        min = x


t = int(input())
for tc in range(1, t+1):
    day, month_1, month_3, year = map(int, input().split())
    use = list(map(int, input().split()))
    min = 999999
    day_month_1 = month_1//day
    fee = [0] * 12
    for i in range(12):     # day와 month_1 처리
        if use[i] > day_month_1:
            fee[i] = month_1
        else:
            fee[i] = use[i] * day
    total_fee = sum(fee)
    change(total_fee, 0) # month_3을 처리해주는 함수
    if min > year:
        min = year
    print('#%d' %tc, min)