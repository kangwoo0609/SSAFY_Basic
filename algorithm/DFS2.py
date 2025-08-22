# 출력: 0 1 4 5 2 3 6 7 8
def dfs(now):
    print(now, end=' ')
    # now 에서 갈 수 있는 노드들을 모두 탐색
    for next_node in graph[now]:
        # next_node를 방문했다면
        if visited[next_node]:
            continue

        visited[next_node] = 1  # next_node 방문처리
        dfs(next_node)



N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 양방향 그래프

visited = [0] * N  # 각 노드에 방문 여부
visited[0] = 1  # 출발점은 방문했다고 가정하고 시작
dfs(0)  # A부터 출발


'''
입력
9 8
0 1
0 2
0 3
1 4
1 5
3 6
3 7
3 8
'''