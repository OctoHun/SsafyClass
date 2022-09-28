t = int(input())
arr = [list(map(int, input().split())) for _ in range(t)]
ans = [0] * t
for i in range(t):
    cnt = 0
    temp = [0] * t
    for j in range(5):
        for l in range(t):
            if i != l and arr[i][j] == arr[l][j]:
                temp[l] += 1
    for j in range(t):
        if temp[j] > 0:
            cnt += 1
    ans[i] = cnt
maxindex = 0
for i in range(t):
    if ans[maxindex] < ans[i]:
        maxindex = i
print(maxindex + 1)