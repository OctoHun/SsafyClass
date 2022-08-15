t = int(input())
for i in range(1, t+1):
    n = int(input())
    cnt = [0] * 1001
    max = 0
    for j in range(n):
        arr = list(map(int, input().split()))
        cnt[arr[2]] += 1
        if arr[0] == 1:
            for k in range(arr[1], arr[2]):
                cnt[k] += 1
        elif arr[0] == 2:
            for k in range(arr[1], arr[2], 2):
                cnt[k] += 1
        elif arr[0] == 3 and arr[1] % 2 == 0:
            for k in range(arr[1], arr[2]):
                if k % 4 == 0:
                    cnt[k] += 1
        else:
            for k in range(arr[1], arr[2]):
                if k % 3 == 0 and k % 10 != 0:
                    cnt[k] += 1
    for j in cnt:
        if j > max:
            max = j
    print('#%d' %i, max)

