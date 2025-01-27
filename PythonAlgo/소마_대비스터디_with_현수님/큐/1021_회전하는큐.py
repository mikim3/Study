# 시작시간 2200 마무리시간  2300
from collections import deque

# 1번 popleft
# 2번 ㅇ왼쪽으로 통쨰로 이동 
# 3번 오른쪽으로 통째로 이동

# n크기의 큐에 popleft를 하는데
# 원하는 원소의 index값이 두번째 줄에 주어진다. 그것들을 popleft해라
# 단 2,3번 즉 위치이동을 최소화 시켜라

# 잘 수행하기 위해서는 
# queue_1 의 현재 첫번째 원소위치에 

# 큐의 크기, 뽑아내려고 하는 수의 개수
n, m = map(int, input().split())
li = list(map(int,input().split()))

for i in range(m):
  li[i] = li[i] - 1  # 인덱스 값이랑 같아짐
queue = deque()
for i in range(n):
  queue.append(i)

count = 0 # 2,3 번 사용 횟수
for i in range(m):
  while True:
    # 목표값 맨앞으로 이동
    if li[i] == queue[0]:
      queue.popleft()
      break
    # 목표 값의 현재위치 탐색
    dest_index = 0
    for j in range(len(queue)):
      if queue[j] == li[i]:
        dest_index = j # dest_index 목표하는 값 의 위치
    if dest_index <= len(queue) // 2:  # 목표가 왼쪽이면
      tmp_queue = deque()
      for j in range(dest_index):
        tmp_queue.append(queue.popleft()) # 2번동작 수행 인덱스 크기만큼 수행 
        queue.append(tmp_queue.popleft()) # 2번동작 수행위해 오른쪽에 추가
        count += 1
    else:
      tmp_queue = deque()
      for j in range(len(queue) - dest_index):  # 오른쪽으로 수행
        tmp_queue.appendleft(queue.pop())
        queue.appendleft(tmp_queue.pop())
        count+=1
print(count)