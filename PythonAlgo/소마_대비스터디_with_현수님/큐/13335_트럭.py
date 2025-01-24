# 시작시간 0930 마무리시간 1015
# sum을 안 쓰고 변수 저장하면 되는 문제를 sum을 사용해서 에러가 났음

from collections import deque

# queue 에서 popleft 하면 모든 값이 앞으로 한칸씩 땡겨짐 <= 차가 한칸 간 것과 같음

# 차 갯수, 다리길이, 최대하중
n, w, L = map(int , input().split())
li = list(map(int,input().split()))
queue = deque()  # 다리를 큐로 표현
for i in range(100000):
  queue.append(0)
count = 0 # 시간 체크
cur_weight = 0
i = 0
while True:
  cur_weight -= queue.popleft()
  # 차가 진입하기 위한 조건
  if i < n:
    if cur_weight + li[i] <= L:
      queue[w-1] = li[i]
      cur_weight += li[i]
      i += 1
  count+=1
  # 더 이상 갈 차도 없고 큐도 비워짐
  if cur_weight == 0 and len(li) <= i:  
     break    
print(count)
  