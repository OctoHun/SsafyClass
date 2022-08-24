def bfs(g, start, n):   # g: 그래프, start: 시작지점, n: 정점개수
    # 중복 탐색 방지를 위한 방문 배열
    visited = [False] * (n + 1) # 인덱스가 몇부터 시작인지 잘 살펴야 한다.
    # 정점 번호가 1부터 시작하면 n + 1
    # 정점 번호가 0부터 시작하면 n
    q = []
    q.append(start) # 탐색을 시작할 초기 위치를 큐에 추가
    visited[start] = True # 초기 위치는 방문했다고 체크

    # 반복을 계속 하는데
    # 초기에 탐색 시작 위치를 넣어주고 반복을 진행하기 때문에,
    # 탐색 위치가 남아있다면 큐가 비어있을 일이 없다.
    # 만약 큐가 비었다면 탐색이 끝난것이다.
    while q:    # 배열 안에 값이 있다면
        t = q.pop(0) #큐에서 맨 앞의 원소 가져오기
        print(t, end = ' ')
        # 현재 위치인 t에서 갈 수 있는 정점들이 있는지 검사
        for i in g[t]:
            if not visited[i]: # 다음 정점 i를 방문한 적이 없다 ==> 탐색 대상이 되고 탐색 대상은 큐에 추가
                # 큐에 추가 한 후에 탐색했다 라는 표시를 하기 위해서 방문배열에 체크
                q.append(i)
                visited[i] = True



g = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 7],
    [2, 6],
    [2, 6],
    [4, 5, 7],
    [3, 6]
]

bfs(g, 1, 7)
