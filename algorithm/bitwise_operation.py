# 비트 연산 많이 쓰나요 ??
# - 운영체제 개발, 하드웨어 파트
#   - 컴퓨터(데스크탑, 노트북) X -> 우리 프로그램을 보드에 담아야 한다.
#   - 최적화를 굉장히 잘해주어야 한다.
#     - 비트 단위로 메모리 계산


# 우리는 비트 연산을 활용한 실제 개발은 하지 않는다
# - 알고리즘 때 활용
#   - 부분 집합관련 문제를 풀 때 활용

print(1)
print(1 << 1)
print(1 << 2)  # 1번 왼쪽으로 밀 때마다 2배 씩 늘어난다.

# 우리는 부분 집합 문제에서 활용한다
arr = [1, 2, 3, 4]
N = len(arr)

# 1. 부분 집합의 개수
print(f"arr 로 만들 수 있는 부분 집합의 수 = {1 << N}")

# 2. 전체 부분 집합을 계산
for i in range(1 << N):  # 전체 부분 집합을 하나 씩 모두 고려
    print(f"i = {i} / {i:04b}")
    for j in range(N):  # 각 자리가 현재 부분 집합에 들어가는가 ?
        if i & (1 << j):
            print(arr[j], end=' ')
    print()

print('----------------------------')
# 10개의 정수에서 부분집합의 합이 0이 되는 부분 집합을 모두 출력하기

arr = [-7, -5, 2, 3, 8, -2, 4, 6, 9]
N = len(arr)

for i in range(1, 1 << N):  # 512개의 부분집합을 모두 확인
    subset = []
    total = 0
    for j in range(N):
        if i & (1 << j):  # i번 째 부분 집합에 해당 원소가 포함되는 지 체크
            subset.append(arr[j])
            total += arr[j]
    if total == 0:
        print(subset)

print('----------------------------')

arr = [-7, -5, 2, 3, 8, -2, 4, 6, 9]
N = len(arr)


# 시작점: index 0 / 종료지점: index len(arr)
# 누적값: index, 부분집합(subset), total
def recur(index, subset, total):
    if index == N:  # 종료 조건 (모든 원소를 다 고려함)
        if total == 0:
            print(subset)
        return

    # index 번 째 원소를 집합에 포함 시킨 경우
    recur(index + 1, subset + [arr[index]], total + arr[index])
    # index 번 째 원소를 집합에 포함시키지 않은 경우
    recur(index + 1, subset, total)


recur(0, [], 0)