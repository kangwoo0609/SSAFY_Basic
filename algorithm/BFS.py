def bfs(start):
    q = [start]  # 방문할 후보군들을 저장할 q

    while q:
        now = q.pop(0)
        # visited[now] = 1  # 중복해서 queue 에 삽입되는 비효율적인 방법
        print(now, end=' ')
        
        # N 개의 노드를 모두 확인하면서
        for next_node in range(N):
            # now 에서 갈 수 없으면 continue
            if graph[now][next_node] == 0:
                continue

            # 이미 방문한 노드라면 continue
            if visited[next_node]:
                continue

            visited[next_node] = 1  # 방문처리
            q.append(next_node)     # 후보군에 추가


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
start = 0
visited[start] = 1  # 출발지는 따로 초기화
bfs(start)