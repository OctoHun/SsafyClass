t=int(input())
for i in range(1, t+1):
    tt = int(input())
    c=''
    for j in range(tt):
        a, b = input().split()
        c = c + a * int(b)
    c=list(c)
    print('#%d' %i)
    for k in range(1,len(c)+1):
        print(c[k-1], end = '')
        if k % 10 == 0:
            print('')
    print('')