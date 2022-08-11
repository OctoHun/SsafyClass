t = int(input())
for i in range(1, t+1):
    a = input()
    for j in range(11):
        if a[:j+1] == a[j+1:2*j+2]:
            ans = j+1
            break
    print('#%d' %i, ans)