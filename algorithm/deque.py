# deque: queue 자료구조를 활용할 때 많이 쓰는 패키지
# - 이중연결리스트 구조로 구현되어 있어 앞/뒤 데이터 삽입 삭제가 빠르다: O(1)
# - 일반 리스트
#    - 가장 앞 데이터 삭제 = O(N)
#      - 한 칸 씩 모두 앞으로 당긴다
#    - 가장 앞에 데이터 추가 = O(N)
#      - 한 칸 씩 모두 뒤로 민다
from collections import deque


dq = deque()  # 비어있는 덱을 초기화

# 가장 뒤에 데이터 삽입
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)

# 가장 앞에 데이터 삽입
dq.appendleft(4)
dq.appendleft(5)
print(dq)

print(dq.pop())
print(dq.popleft())