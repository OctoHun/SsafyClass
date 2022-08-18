def delete(s, n):
    global a
    b = ''
    for i in range(n-1):
        if s[i] == s[i+1]:
            b += s[:i]
            if i+2 < n:
                b += s[i+2:]
            delete(b, len(b))
            break
    else:
        a = n
    return 0


t = int(input())
for i in range(1, t+1):
    s = input()
    n = len(s)
    a = 0
    delete(s, n)
    print('#%d' %i, a)