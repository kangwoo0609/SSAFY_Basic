# 함수
# - 코드를 따로 분리했다.
# 왜 ? (목적)
# 1. 재사용성: 코드를 다시 사용하기 위해서
# 2. 가독성: 기능 별로 함수를 분리하면, 가독성이 매우 높아진다.
#   -> 회사에서는 (코드 리뷰, 리펙토링)을 통해 코드를 잘 관리

# 함수 사용법
# - 정의 (def 키워드)
# - 구성요소
    # 1. 함수명
    # 2. 파라미터(매개변수, 인자)
    # 3. 내부 로직

def func():
    x = 10
    # 함수 스코프
    print("func")
    print("func")
    print("func")
    print("func")

# - 호출
func()

print("func 함수 호출 끝")

#------------------------------

def func2(x, y):
    # 함수가 외부 데이터를 필요로 할 때
    # 숫자 2개를 합치는 함수
    # -> 숫자 2개는 외부에서 입력을 받았다.
    print(x + y)

def my_input():
    num1 = int(input())
    num2 = int(input())
    return num1, num2

# 1. my_input 이 입력받은 값을 반환해주고
# 2. func2 데이터를 받아서 결과를 출력
n1, n2 = my_input()
func2(n1, n2)

#-------------------------------

def func3():
    # 함수 스코프 (지역변수)
    print(a, b)
    x, y = 10, 20

    def func4():
        print("func4")
        print(a, b)

        print(x, y)
        c = 10
    func4()

# 전역변수
a = int(input())
b = int(input())

func3()

for i in range(10):
    abcd = 10
print(abcd)


# ---------------------

x = "global"

def outer():
    # 전역변수의 x 를 가져다 쓰겠다
    global x
    x = "outer"       # outer 함수의 지역 변수
    print("1:", x)

    def inner():
        x = "inner"
        print("2:", x)

    inner()
    print("3:", x)

outer()
print("4:", x)

# ----------------------
# 리스트를 파라미터로 전달하면 원본 값이 변경된다.
def func5(li):
    li[0] = 10  # 원본 li의 값도 변경됨
    print(li)

arr = [1, 2, 3]
func5(arr)
print(arr) # [10, 2, 3]


def func6():
    # li 라는 지역변수를 새로 만듦 (원본 li 는 수정안됨)
    li = [4, 5, 6] # 선언
    print(li)

li = [1, 2, 3]
func5()
print(li)