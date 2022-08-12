for _ in range(10):
    t = int(input())
    p = input()
    s = input()
    ans = 0
    for i in range(len(s)-len(p)+1):
        cnt = 0
        for j in range(len(p)):
            if p[j] != s[j+i]:
                break
            cnt += 1
        if cnt == len(p):
            ans += 1

    print('#%d' %t, ans)