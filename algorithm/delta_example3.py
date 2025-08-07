# 우하좌상 델타 배열
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count = 0
    way = 0
    ni = 0
    nj = 0
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    for i in range(N*N):
        arr[ni][nj] = i+1

        # 다음 좌표 후보
        next_i = ni + di[way]
        next_j = nj + dj[way]

        # 방향을 틀어야 할 조건
        # - 범위를 벗어났거나, 숫자를 만났다면
        if next_i < 0 or next_i >= N or next_j < 0 or next_j >= N or arr[next_i][next_j] != 0:
            # way 는 0, 1, 2, 3 을 반복
            way = (way + 1) % 4
        
        # 이동
        ni = ni + di[way]
        nj = nj + dj[way]

    
    print(f"#{test_case}")
    for i in arr:
        print(" ".join(map(str, i)))