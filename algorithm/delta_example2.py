# SWEA 경건한 파리채 문제

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1] # 어차피 델타 관련은 항상 안 변함

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_result = 0
    ry, rx = 0, 0

    # 전체 이차원 리스트를 순회하면서
    for y in range(N):
        for x in range(N):
            # 상하좌우 값들을 더해준다.
            result = arr[y][x]  # 현재좌표

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                # 범위 밖으로 나가면, 해당 방향은 계산 X
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                result += arr[ny][nx]

            # 최대값 갱신
            if max_result < result:
                max_result = result
                ry = y
                rx = x

    print(f'#{tc} {max_result} {ry} {rx}')