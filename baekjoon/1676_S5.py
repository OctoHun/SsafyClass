N = int(input())
result = 1
for i in range(1, N+1):
    result *= i
result = str(result)
length = len(result)
cnt = 0
for i in range(length-1, -1, -1):
    if result[i] != '0':
        break
    cnt += 1
print(cnt)