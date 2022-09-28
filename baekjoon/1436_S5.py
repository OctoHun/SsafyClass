n = int(input())
cnt = 0
a = 665
while n != cnt:
    for i in range(10000):
        a += 1
        if '666' in str(a):
            break
    cnt += 1
print(a)