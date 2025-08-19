T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    now = 1
    cnt = 0

    while now < N:
        if arr[now] == 0:
            now += 1
        else:
            next_idx = arr[now]  # 다음에 이동할 인덱스 저장
            arr[now] = 0  # 0으로 초기화 (한 번 방문했다는 뜻)
            now = next_idx  # now 를 인덱스로 이동
        cnt += 1
    print(f'#{tc} {cnt}')