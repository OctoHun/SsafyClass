t = int(input())
for i in range(1, t+1):
    n = list(map(int, input()))
    cnt = 0
    result = 1
    for j in range(len(n)):
        if n[j] == result:
            cnt += 1
            if result == 1:
                result = 0
            else:
                result = 1
    print('#%d' %i, cnt)