t = int(input())
for i in range(1, t+1):
    arr = [input() for _ in range(5)]
    ans = ''
    length = [0] * 5
    max = 0
    for j in range(5):
        cnt = 0
        for k in arr[j]:
            cnt += 1
        length[j] = cnt
        if length[j] > max:
            max = length[j]
    for j in range(max):
        for k in range(5):
            if j < length[k]:
                ans += arr[k][j]
    print('#%d' %i, ans)
