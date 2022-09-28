n = int(input())
arrn = list(map(int, input().split()))
m = int(input())
arrm = list(map(int, input().split()))
cnt = {}
for i in range(n):
    if arrn[i] in cnt:
        cnt[arrn[i]] += 1
    else:
        cnt[arrn[i]] = 1
for i in range(m):
    if arrm[i] in cnt:
        print(cnt[arrm[i]], end = ' ')
    else:
        print(0, end = ' ')