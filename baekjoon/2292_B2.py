n = int(input())
cnt = 1
room = 1
while 1:
    if n == 1:
        cnt = 0
        break
    elif n > (room+(cnt*6)):
        room += cnt*6
        cnt += 1
    else:
        break
print(cnt+1)