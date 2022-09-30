def findset(x):
    while x != graph[x]:
        x = graph[x]
    return x


def kruskal(cnt):
    global ans
    x = 0
    while cnt != n-1:
        if findset(arr[x][0]) != findset(arr[x][1]):
            graph[findset(arr[x][1])] = findset(arr[x][0])
            ans += arr[x][2]
            cnt += 1
        x += 1


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    totaln = 0
    for i in range(n, 0, -1):
        totaln += i
    arr = [[0]*3 for _ in range(totaln)]
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    cnt = 0
    for j in range(n):
        for k in range(j+1, n):
            if j != k:
                arr[cnt][0] = j
                arr[cnt][1] = k
                arr[cnt][2] = (x[j]-x[k])**2+(y[j]-y[k])**2
                cnt += 1
    graph = [0]*n
    ans = 0
    for i in range(n):
        graph[i] = i
    arr.sort(key=lambda x:(x[2]))
    kruskal(0)
    print('#%d' %tc, round(ans*E))