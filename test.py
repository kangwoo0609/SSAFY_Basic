# 문제풀이 시 입력
# input(): 콘솔 입력. 항상 문자열로 들어옴
# 문자열 -> 숫자로 바꿔주어야 한다 (형변환)
number = input()
int_number = int(number)
print(f'number = {number}')

print(int_number + 5)

# --------------------------
# a b - 2개의 문자 입력
# split(): 공백을 기준으로 리스트로 분리하여 저장
word = input().split()
print(word[0])
print(word[1])

# ---------------------
# 10 20 - 2개의 숫자 입력
# 각 요소에 대해서, 정수 변환 작업을 수행
# map(함수, 반복할 객체) : 각 요소에 함수를 적용
# -> 수요일에 함수 파트에서 다시 한 번 설명
numbers = list(map(int, input().split()))
print(numbers)  # [10, 20]
print(numbers[0]) # 10
print(numbers[1]) # 20