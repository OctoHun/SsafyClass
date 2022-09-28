cnt = 0
arr = [2] * 10000
for i in range(10000):
    a = input()
    if a == '0':
        break
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            arr[cnt] = 0
            break
        else:
            arr[cnt] = 1
    cnt += 1
for j in range(i):
    if arr[j] == 0:
        print('no')
    else:
        print('yes')
