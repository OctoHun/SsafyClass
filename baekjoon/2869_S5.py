a, b, v = map(int, input().split())
x = v-a
y = a-b
temp = x//y
now = temp * y + a
cnt = temp+1
while now < v:
    now -= b
    now += a
    cnt += 1
print(cnt)
