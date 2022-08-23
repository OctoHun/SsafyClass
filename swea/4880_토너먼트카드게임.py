def rsp(a, b):
    if (a != b + 2 and a > b) or a == b or a + 2 == b:
        return 1
    else:
        return 0


def compare(start, n):
    global winner, index, card
    if (n - start + 1) == 1:
        winner[index] = winner[n]
        index += 1
        return
    elif (n - start + 1) == 2:
        if rsp(card[winner[start]], card[winner[n]]):
            winner[index] = winner[start]
            index += 1
            return
        else:
            winner[index] = winner[n]
            index += 1
            return
    else:
        compare(start, (n + start)//2)
        compare((n + start)//2 + 1, n)


t = int(input())
for i in range(1, t+1):
    n = int(input())
    card = list(map(int, input().split()))
    winner = [-1] * n
    for j in range(n):
        winner[j] = j
    while 1:
        index = 0
        compare(0, n-1)
        if index == 1:
            ans = winner[0]
            break
        else:
            n = index
    print('#%d' %i, ans+1)