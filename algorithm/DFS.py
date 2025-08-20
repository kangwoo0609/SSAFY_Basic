def dfs(prev, now):
    print(prev, now)
    # N 개의 노드를 모두 확인하면서
    for next_node in range(N):
        # 다음 노드가 연결이 안되어 있으면 가지 않는다.
        if graph[now][next_node] == 0:
            continue

        # 이미 방문한 next_node 라면 continue
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(now, next_node)



N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
start = 0
visited[start] = 1  # 출발지는 따로 초기화
dfs(0, start)