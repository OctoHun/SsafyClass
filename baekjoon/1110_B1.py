n = input()
result = ''
if int(n) < 10:
    n += '0'
result += n
cnt = 0
while 1:
    a = str(int(n[0]) + int(n[1]))
    if int(a) < 10:
        n = n[1] + a
    else:
        n = n[1] + a[1]
    cnt += 1
    if result == n:
        break
print(cnt)