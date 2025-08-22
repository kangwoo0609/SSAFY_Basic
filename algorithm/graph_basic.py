# 인접 행렬

N, M = map(int, input().split())


# 1. 인접 행렬 방식 ----------------------------
# 0으로 초기화된 9*9 리스트
# graph = [[0] * N] * N  # 얕은 복사 주의!!!!!
# graph[0][1] = 99  # 얕은 복사가 발생하면, 각 리스트에 서로 영향
# print(graph)
# 아래 처럼 선언해야 얕은 복사가 발생하지 않는다.
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1  # 양방향 그래프

for i in range(N):
    print(graph[i])


# 인접 리스트

graph = [[] for _ in range(N)]


for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 양방향 그래프

for i in range(N):
    print(graph[i])