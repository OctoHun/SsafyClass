def p(cnt, arr):
    if cnt == 5:
        print(arr)
        return
    p(cnt+1, arr+[a[cnt]])
    p(cnt+1, arr)


def c(cnt, arr):
    if cnt == 5:
        print(arr)
        return
    for i in range(5):
        if visit[i] == 0:
            visit[i] = 1
            c(cnt+1, arr+[a[i]])
            visit[i] = 0



a = [1, 2, 3, 4, 5]
# p(0, [])
visit = [0]*5
c(0, [])