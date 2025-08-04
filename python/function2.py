# map(함수, 반복객체)
# - 각 요소에 함수를 적용해주는 역할

# 각 요소에 5를 더한 값을 적용해서, 새로운 리스트
def func(n):
    return n + 5

arr = [1, 2, 3]
result = list(map(func, arr))
print(result) # [6, 7, 8]


# 각 요소의 합을 저장하는 새로운 리스트
def func2(n1, n2):
    return n1 + n2

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
result2 = list(map(func2, arr1, arr2))
print(result2)

# lambda 와 함께 활용하는 방법
# - 이름 리스트 -> key 값이 name 인 dictionary 를 구현해서, list 로 반환
names = ['금기륜', '이강우', '오규태']
ages = [40, 30, 20]

# lambda <parameter>: <return 값>
# names 와 ages 요소를 하나씩 name 와 age 에 담는다.
result3 = list(map(lambda name, age: 
                   {'name': name, 'age': age}, names, ages))
print(result3)