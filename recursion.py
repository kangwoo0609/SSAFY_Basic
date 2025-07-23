# 재귀 함수
# - 자기 자신을 호출하는 함수


# 무한 루프 (대략 1,000번 제한)
def func():
    func()

# 재귀 함수의 필수 구성요소
# 1. 종료 시점
# 2. 시작값, 누적값
# 3. 나머지 구현
#  - 다음 호출 전
#  - 다음 호출
#  - 돌아왔을 때

# ex) 1 2 3 4 5 5 4 3 2 1 출력하는 함수

def recur(num):
    if num == 6:
        print(num, end=' ')
        return

    print(num, end=' ')
    recur(num + 1)
    print(num, end=' ')

recur(1)

# 팩토리얼 예제
# - return 을 활용하는 버전이 이해하기 쉽다
def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

factorial(5)
# 5! -> 5 * 4 * 3 * 2 * 1
# --> 5 * 4!
# 시작 : 5
# 끝 : 1