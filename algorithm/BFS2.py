from collections import deque


def bfs(start):
    # queue 에 들어가는 데이터 == 앞으로 방문해야 할 후보군
    dq = deque([start])

    while dq:
        now = dq.popleft()
        print(now, end=' ')

        # now 에서 갈 수 있는 노드들을 모두 보면서
        # - 이미 방문했다면 continue
        # - 방문처리 + dq 에 삽입
        for next_node in graph[now]:
            if visited[next_node]:
                continue

            visited[next_node] = 1
            dq.append(next_node)


N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 양방향 그래프

visited = [0] * N  # 각 노드에 방문 여부
visited[0] = 1  # 출발점은 방문했다고 가정하고 시작
bfs(0)


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