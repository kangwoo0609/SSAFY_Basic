# 가지치기 예시

N = 4


def recur(cnt, result):
    if cnt > N:  # 모든 숫자를 고려 했다면
        print("result = ", *result)
        return

    # 현재 숫자를 부분 집합에 포함한 경우
    recur(cnt + 1, result + [cnt])

    # 현재 숫자를 부분 집합에 포함하지 않은 경우
    recur(cnt + 1, result)


recur(1, [])