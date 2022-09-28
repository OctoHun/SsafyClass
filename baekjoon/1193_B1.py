n = int(input())
a = 1
result = 0
while 1:
    result += a
    if result >= n:
        break
    a += 1
if a % 2 == 0:
    ans1 = result - n + 1
    ans2 = n - result + a
else:
    ans1 = n - result + a
    ans2 = result - n + 1

print(ans2, end = '')
print('/', end = '')
print(ans1)