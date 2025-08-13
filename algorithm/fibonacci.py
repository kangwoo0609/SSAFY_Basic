# 피보나치5
def fibonacci(n):
    # 종료조건
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


N = int(input())
print(fibonacci(N))

#-------------------------------------------------------
#-------------------------------------------------------


# 피보나치 2

memo = {}

def fibonacci(n):
    # 종료조건
    if n <= 1:
        return n

    # 이미 계산했던 것인가 ?
    if memo.get(n):
        return memo[n]  # 기존에 기록 해놓은 값을 return

    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]


N = int(input())
print(fibonacci(N))