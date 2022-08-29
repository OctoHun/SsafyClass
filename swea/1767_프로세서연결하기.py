def dfs(c, core_cnt, connect):
    global ans, arr
    if c == core_cnt:   # 탐색을 진행한 코어의 갯수와 코어의 총 갯수가 같다면
        elect = 0
        for j in range(n):
            for k in range(n):
                if arr[j][k] == 2:
                    elect += 1
        if connect > ans[1]:    # 저장된 코어의 탐색 갯수보다 지금 탐색하여 알아낸, 연결된 코어의 갯수가 더 크다면 무조건 새로 바꿔줌
            ans[0] = elect
            ans[1] = connect
        elif connect == ans[1] and elect < ans[0]: # 연결된 코어의 갯수는 같은데 더 짧은 경로라면 경로의 길이 바꿔줌
            ans[0] = elect

        return
    j, k = core[c]

    cnt = 0
    for a in range(k):  # 왼쪽부터 core위치까지 1 없으면 연결 가능
        if arr[j][a] != 0:
            break
        else:
            cnt += 1
    if cnt == k:
        for a in range(k):
            arr[j][a] = 2
        dfs(c+1, core_cnt, connect + 1)
        for a in range(k):
            arr[j][a] = 0

    cnt = 0
    for a in range(k+1, n):  # 오른쪽 탐색
        if arr[j][a] != 0:
            break
        else:
            cnt += 1
    if cnt == n - k - 1:
        for a in range(k+1, n):
            arr[j][a] = 2
        dfs(c+1, core_cnt, connect + 1)
        for a in range(k+1, n):
            arr[j][a] = 0

    cnt = 0
    for a in range(j-1, -1, -1):  # 위 탐색
        if arr[a][k] != 0:
            break
        else:
            cnt += 1
    if cnt == j:
        for a in range(j-1, -1, -1):
            arr[a][k] = 2
        dfs(c + 1, core_cnt, connect + 1)
        for a in range(j-1, -1, -1):
            arr[a][k] = 0

    cnt = 0
    for a in range(j+1, n):  # 아래 탐색
        if arr[a][k] != 0:
            break
        else:
            cnt += 1
    if cnt == n - j - 1:
        for a in range(j+1, n):
            arr[a][k] = 2
        dfs(c + 1, core_cnt, connect + 1)
        for a in range(j+1, n):
            arr[a][k] = 0
    dfs(c+1, core_cnt, connect)



T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    core = [0] * 12
    cnt = 0
    ans = [999, 0]
    for j in range(n):  # core 변수에 1이 들어있는 위치값 저장
        for k in range(n):
            if arr[j][k] == 1 and j != 0 and j != n-1 and k != 0 and k!= n-1:
                core[cnt] = j, k
                cnt += 1
    core_cnt = cnt
    dfs(0, core_cnt, 0)
    print("#%d" % test_case, ans[0])