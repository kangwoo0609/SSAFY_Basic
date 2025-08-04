# 실제 연산: 1000번
# 빅오 표기법: O(N)
N = 1000
for i in range(N):
    pass


# 실제 연산: 100 * 1000
# 빅오 표기법: O(N)
#  - 앞에 붙는 상수들(고정된 시간)은 모두 생략하고 표기
for _ in range(100000):
    for i in range(N):
        pass

# 빅오 표기법: O(N^2)
for _ in range(N):
    for _ in range(N):
        pass

# -----------------

# 입력 변수가 2개인 경우
# - 빅오 표기법: O(N + M)
N = 100
M = 1000

for _ in range(N):
    pass

for _ in range(M):
    pass

# --------------
# 빅오 표기법: O(N * M)
for _ in range(N):
    for _ in range(M):
        pass

# ---------------
N = int(input())
# 연산 횟수가 입력에 관계없이 고정되어 있는 로직
# 빅오 표기법: O(1) - 상수번 호출한다.
for _ in range(100):
    pass

for _ in range(10000):
    pass

for _ in range(1000000):
    pass

for _ in range(100000000):
    pass

# ----------------------
# 빅오표기법: O(logN)
# - 숫자가 두 배 씩 늘어나거나, 반 씩 줄어드는 경우 logN 인 경우가 많다.
N = 1000
i = 1
while i < N:
    print(i)
    i *= 2