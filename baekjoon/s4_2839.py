def abc(a, b):
    global ans
    c = n - ((a*5) + (b*3))
    if c == 0:
        if a < 0 or b < 0:
            ans = -1
            return
        ans = a+b
        return
    else:
        abc(a-1, (n-(a-1)*5)//3)


n = int(input())
ans = 0
abc(n//5, (n%5)//3)
print(ans)