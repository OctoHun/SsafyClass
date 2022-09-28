n = int(input())
result = ['D'] * n
for i in range(n):
    acard = [0] * 5
    bcard = [0] * 5
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for j in range(a[0]):
        acard[a[j+1]] += 1
    for j in range(b[0]):
        bcard[b[j+1]] += 1
    for j in range(4, 0, -1):
        if acard[j] > bcard[j]:
            result[i] = 'A'
            break
        elif acard[j] < bcard[j]:
            result[i] = 'B'
            break
for i in range(n):
    print(result[i])
