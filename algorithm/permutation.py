# ----------------------- 순열 (한 번 사용한 숫자는 사용할 수 없음)


N = 4
result = []
visited = [0] * (N + 1)  # 숫자 1~4 사용 여부를 기록


def recur(cnt):
    if cnt > N:  # 모든 숫자를 고려 했다면
        print("result = ", *result)
        return

    for i in range(1, N + 1):
        if visited[i]:  # i 라는 숫자를 이미 활용했다면 넘어가라
            continue

        result.append(i)
        visited[i] = 1
        recur(cnt + 1)
        visited[i] = 0
        result.pop()


recur(1)