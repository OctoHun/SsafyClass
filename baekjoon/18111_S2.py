import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr = [0]*257
max = 0
min = 999
for i in range(n):
    for j in range(m):
        arr[ground[i][j]] += 1
        if ground[i][j] > max:
            max = ground[i][j]
        if ground[i][j] < min:
            min = ground[i][j]
sum = 0
temp_b = b
min_t = 999999999
height = 0
for i in range(min, max+1):
    avg = i
    for j in range(max, avg, -1):
        sum += (j-avg)*2*arr[j]
        temp_b += (j-avg)*arr[j]
    for j in range(min, avg):
        sum += (avg-j)*arr[j]
        temp_b -= (avg-j)*arr[j]
        if temp_b < 0:
            break
    if temp_b >= 0 and sum <= min_t:
        min_t = sum
        height = avg
    sum = 0
    temp_b = b
print(min_t, height)