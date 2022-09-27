def max_num(a, b): # 유클리드 호제법 - 최대공약수를 구하는 알고리즘
    global c
    if a%b == 0:
        print(b)
        c = b
        return
    max_num(b, a%b)


a, b = map(int, input().split())
c = 0
if a < b:
    a, b = b, a
max_num(a, b)
ans = a*b//c
print(ans)