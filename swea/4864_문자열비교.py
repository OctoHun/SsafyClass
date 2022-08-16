t = int(input())
for i in range(1, t+1):
    a = input()
    b = input()
    ans = 0
    for j in range(len(b)-len(a)+1):
        cnt = 0
        for k in range(len(a)):
            if a[k] != b[k+j]:
                break
            else:
                cnt += 1
        if cnt == len(a):
            ans = 1
    print('#%d' %i, ans)