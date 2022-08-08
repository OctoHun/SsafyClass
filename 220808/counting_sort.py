a = [7, 6, 0, 5, 8, 9, 3, 2]
b = [0] * 8
cnt = [0] * 10
# DAT 만듬
for i in a:
    cnt[i] += 1

# 정렬 인덱스를 맞춰주기 위해 전 인덱스에 나의 인덱스를 더해준다.
for i in range(len(cnt)-1):
    cnt[i+1] += cnt[i]

# 뒤에서부터 정렬 후 해당 숫자를 index로 하는 cnt 값 감소
for i in range(len(a)-1, -1, -1):
    b[cnt[a[i]]]=a[i]