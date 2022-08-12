t = int(input())
for i in range(1, 1+t):
    P, Q, R, S, W = map(int, input().split())
    Afee=0
    Bfee=0
    Afee=W*P
    if W<=R:
        Bfee=Q
    else:
        Bfee=Q + (W-R) * S
    if Afee>Bfee:
        print('#%d' %i, Bfee)
    else:
        print('#%d' %i, Afee)
