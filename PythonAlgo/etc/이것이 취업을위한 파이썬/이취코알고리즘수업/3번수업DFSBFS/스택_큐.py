stack = []

#삽입
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()  #가장 최상위 스택 삭제
stack.append(1)
stack.append(4)
stack.pop()  #가장 최상위 스택 삭제

print(stack[::-1])  # 최상단 원소부터 출력
print(stack)  


# 큐 구현을 위해 deque 라이브러리 사용
# 큐 : 먼저들어온게 먼저나가는 선입선출
# 그림으로는 왼쪽으로 오른쪽으로 차례대로 박스가 오는가는 터널처럼 생각하자
# 나갈때도 가장오른쪽에 있는 먼저들어온 것이 먼저 나간다.

from collections import deque

queue = deque()

#
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 아까 이해한 것과는 반대(left)가 반대   어찌됐든 기억해야할것은 선입선출이라는 것이고 popleft()라는 함수를 기억하자
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순서대로 출력
queue.reverse()  # 역순으로 바꾸기
print(queue)  # 나중에 들어온 워노부터 출력
