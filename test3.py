a = [1, 2, 3]
b = a  # 참조 복사 (메모리 복사)
        # 같은 객체를 가리킨다.
b[0] = 10
print(f'a = {a}')
print(f'b = {b}')
print(a is b)
print(id(a))
print(id(b))


a = [[1, 2], [3, 4]]

# 깊은 복사
# - 메모리가 완전히 다른 곳에
#  새로운 객체를 저장하겠다.
import copy
b = copy.deepcopy(a)
b[0][0] = 10
print(a)
print(b)
print(id(a))
print(id(b))

# 얕은 복사
# - 표지만 복사한 개념 (속 페이지는 공유)
# - 껍데기는 따로 쓰고, 속은 함께 쓰자
c = [1, [2, 3]]
d = c.copy()
print(id(c))
print(id(d))
d[0] = 10
print(c) # [1, [2, 3]]
print(d) # [10, [2, 3]]
print(id(c[1]))
print(id(d[1]))  # 둘은 같은 주소
d[1][0] = 30
print(c) # [1, [30, 3]]
print(d) # [10, [30, 3]]