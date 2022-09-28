arr = list(map(int, input().split()))
for i in range(1, 1000000):
    cnt = 0
    for k in range(5):
        if i % arr[k] == 0:
            cnt += 1
    if cnt > 2:
        ans = i
        break
print(ans)