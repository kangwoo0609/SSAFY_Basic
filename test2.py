# Set
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b) #합집합
print(a & b) #교집합
print(a - b) #차집합
print(a ^ b) #대칭차집합, a, b 각자에만 있는 것 == 겹치지 않는 부분

e = {1, 2}
f = {2, 1}

print(e == f)

g = {1, 2}
h = {1, 2, 3, 4}
print(g < h)

# Dictionary - key:value 쌍으로 저장
# 리스트로 저장할 수 있는 모든 데이터는 딕셔너리로 표현할 수 있다.
# -> 리스트: 순서로 표현하면 더 좋을 때
# -> 딕셔너리: 순서가 없고, key 값을 통한 조회가 많을 때

di = {}

person = {'name': '이강우',
          'age' : 26,
          }
# list, set, dict 등 가변한 자료형은 key로 설정 불가

di['이름'] = 'value'
# 한번에 여러개 key value 넣는 건 불가 >> 나중에 tuple 머시기로 가능하다고 함
key = '이름'
print(di[key])

# 없는 키 값을 조회하면 다 에러남
# 키 값이 유무 검사
print(di.get('이름')) # 있으면 value 출력
print(di.get('non')) # 없으면 None 출력



# List
numbers = []# 비어있는 set 정의
c = set()
d = {}
print(type(c))
print(type(d))

# 집합 연산 활용하기
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)  # 합집합 - {1, 2, 3, 4}
print(a & b)  # 교집합 - {2, 3}
print(a - b)  # 차집합
print(a ^ b)  # 대칭차집합

# e 와 f 는 같은 값
# - set은 순서를 신경쓰지 않는다.
e = {1, 2}
f = {2, 1}
print(e == f)

# 비교 연산자를 통해서 부분집합 여부를 알 수 있다.
g = {1, 5}
h = {1, 2, 3, 4}

print(g < h)


# dictionary - key:value 쌍으로 저장하기 위해
# - 리스트로 저장할 수 있는 모든 데이터는 딕셔너리로 표현할 수 있다.
# -> 리스트: 순서가 있으면 더 좋을 때 (만약 성적표 -> 상위3명을 뽑아야한다.)
# -> 딕셔너리: 순서가 없고, key 값을 통한 조회가 많을 때 (이름:점수)

# 딕셔너리 활용

# 초기값을 넣어주면서 선언
# - key 값은 불변 데이터만 가능 (list 는 불가능하다!)
# - key 값이 변동 -> 해시값이 변동 -> 메모리 비효율적이다!
#  - 자료구조 시간에 자세하게 다루겠습니다.
person = {
    "name": "금기륜",
    20: "test",
    (1, 2): "test"
}
print(person)

di = {}
di["이름"] = "금기륜"  # 추가
print(di)
di["이름"] = "홍길동"  # 재할당 (이미 있는 key값)
print(di)
key = "이름"
print(di[key])  # 특정 key 값을 통해 데이터 조회
# print(di["없는 키값"])  # 없는 키 값을 조회하면 에러난다

# 키 값이 있는 지 검사
print(di.get(key))  # 있는 키 값: value 를 출력
print(di.get("없는 키값")) # 없는 키 값: None을 출력
                          # 조건문을 배우고 나면, 에러 처리를 수동으로 가능하게 할 수 있다.


# key, value, key & value 출력하는 법
print(di.keys())
print(di.values())
print(di.items())


# 리스트 활용
numbers = []

numbers.append(3)  # append: 가장 뒤에 데이터를 추가
numbers.append(2)
numbers.append(1)
numbers.append(5)
print(numbers)  # [3, 2, 1, 5]

print(numbers[0]) # 가장 앞 데이터
print(numbers[-1]) # 가장 뒤 데이터

print(numbers[0:2])  # [3, 2]
print(numbers[::2])  # [3, 1]
print(numbers[1::2])  # [2, 5]

# 데이터 삭제
numbers.pop()  # pop(): 맨 뒤의 데이터 삭제
print(numbers)  # [3, 2, 1]
numbers.pop(1) # pop(index): index 번째가 삭제
print(numbers) # [3, 1]

numbers.append(3)
numbers.append(2)
numbers.append(1)
numbers.append(5)
print(numbers)

print(numbers[0])
print(numbers[-1])
print(numbers[0:2])
print(numbers[1::2])

numbers.pop() # 맨 뒤의 데이터를 빼서 삭제하는 기능
print(numbers)