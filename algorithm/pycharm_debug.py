# 중단점(breakpoint): 중단점 코드 직전까지 실행 후, 대기 상태


# 디버그 툴 사용법
# - 중단점 기준으로 1줄 씩 실행
#   - F7: 함수 내부로 이동하여 한 줄 씩 실행
#   - F8: 함수 내부로 들어가지 않고, 한 줄 씩 실행
# - 다음 중단점까지 쭉 실행
#   - F9: 다음 중단점까지의 코드들을 모두 실행한 후 대기

def func():
    print("test5")
    print("test6")
    print("test7")


test = 12
print("test1")
print("test2")
print("test3")
num = 10
for i in range(10):
    num += i
    print("test4")  # 4번에서 버그가 발생 -> 6번째 반복에서 버그 발생

func()
func()