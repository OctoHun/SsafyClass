n = input()
start = int(n) - len(n)*9
flag = 0
for i in range(start, int(n)):
    if i > 0:
        ans = i
        temp = str(i)
        for j in range(len(temp)):
            ans += int(temp[j])
        if ans == int(n):
            print(i)
            flag = 1
            break
if flag == 0:
    print(0)