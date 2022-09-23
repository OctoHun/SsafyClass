def seven(y, x, cnt, temp):
    if cnt == 7:
        if temp not in visit:
            visit.append(temp)
        return
    if 0 < x:
        seven(y, x-1, cnt+1, temp+arr[y][x-1])
    if x < 3:
        seven(y, x+1, cnt+1, temp+arr[y][x+1])
    if 0 < y:
        seven(y-1, x, cnt+1, temp+arr[y-1][x])
    if y < 3:
        seven(y+1, x, cnt+1, temp+arr[y+1][x])


t = int(input())
for tc in range(1, t+1):
    arr = [list(input().split()) for _ in range(4)]
    visit = []
    for i in range(4):
        for j in range(4):
            temp = ''
            temp += arr[i][j]
            seven(i, j, 1, temp)
    print('#%d' %tc, len(visit))