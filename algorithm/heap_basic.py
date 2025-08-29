import heapq  # 모듈 불러오기
from heapq import heappush, heappop, heapify  # 파일 안에 클래스, 함수

heap = [4, 15, 19, 11, 20, 13]
heapify(heap)  # python 은 min heap 으로 구현

while heap:
    num = heappop(heap)
    print(num)  # 오름차순 결과 출력

print(heap)  # []
heappush(heap, 15)
heappush(heap, 13)
heappush(heap, 19)
heappush(heap, 11)
heappush(heap, 4)
heappush(heap, 20)
print(heap)  # [4, 11, 19, 15, 13, 20]

# max heap 은 ?
# - 음수를 곱해서 집어넣고, 꺼내서 다시 음수를 곱한다.
heap = []
heappush(heap, -15)
heappush(heap, -13)
heappush(heap, -19)
heappush(heap, -11)
heappush(heap, -4)
heappush(heap, -20)

while heap:
    num = heappop(heap)
    print(-num)