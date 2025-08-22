def dfs(node):
    if node == -1:  # 종료조건: node 번호가 -1이면 끝
        return

    # print(node, end=' ')  # V L R (전위 순회)
    preorder.append(node)
    dfs(graph[node][0])  # 왼쪽 자식으로 이동
    inorder.append(node)
    # print(node, end=' ')  # L V R (중위 순회)
    dfs(graph[node][1])  # 오른쪽 자식으로 이동
    postorder.append(node)
    # print(node, end=' ')  # L R V (후위 순회)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [[] for _ in range(N + 1)]

    for _ in range(N):
        node, left, right = map(int, input().split())
        graph[node].append(left)
        graph[node].append(right)

    preorder = []
    inorder = []
    postorder = []
    dfs(1)

    print(f'#{tc}')
    print(*inorder)
    print(*preorder)
    print(*postorder)