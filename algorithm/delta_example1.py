# SWEA 청구서 계산

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 1. 델타 배열을 만드는 과정
    # - P 개의 입력으로 델타 배열을 초기화
    P = int(input())
    delta = [0] * (N + 1)
    for _ in range(P):
        start, end, cost = map(int, input().split())
        # 변화량을 기록
        delta[start] += cost
        delta[end + 1] -= cost

    # 2. 델타 배열을 활용하는 과정
    current_delta = 0  # 현재 변화량
    for i in range(N):
        current_delta += delta[i]
        arr[i] += current_delta

    print(f"#{tc} {' '.join(map(str, arr))}")