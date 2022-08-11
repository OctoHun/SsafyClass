t = int(input())
for i in range(1, t+1):
    cash = int(input())
    a = [0] * 8
    if cash // 50000 > 0:
        a[0] = cash//50000
        cash = cash%50000
    if cash // 10000 > 0:
        a[1] = cash//10000
        cash = cash%10000
    if cash // 5000 > 0:
        a[2] = cash//5000
        cash = cash%5000
    if cash // 1000 > 0:
        a[3] = cash//1000
        cash = cash%1000
    if cash // 500 > 0:
        a[4] = cash//500
        cash = cash%500
    if cash // 100 > 0:
        a[5] = cash//100
        cash = cash%100
    if cash // 50 > 0:
        a[6] = cash//50
        cash = cash%50
    if cash // 10 > 0:
        a[7] = cash//10
        cash = cash%10
    print('#%d' %i)
    for j in a:
        print(j, end = ' ')
    print()

