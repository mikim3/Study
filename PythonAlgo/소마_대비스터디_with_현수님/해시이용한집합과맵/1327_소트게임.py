# 시작시간 1000 마무리시간

# 만들어진 전체 상태를 확인하면서 BFS를 하는 문제  -> 해쉬 같은게 필요함

from collections import deque

# 현재상태 이동횟수
# visited 

# (현상태, )
# queue = (현상태, 뒤집을 위치???, 횟수)          # 현상태를 뒤집을위치 인덱스에서 뒤집는 다는 의미??
# queue = (현상태, 횟수)

def bfs(li,x):
  queue = deque()
  queue.append((li, 0, 0)) # 이래도 되나?????
  visited = set() # 만든적 있는 상태 저장
  visited.add((queue))  # 이래도 되나??
  
  while queue:
    li_next, now_heksu = queue.popleft()
    # 앞뒤로 이동해보기
    for i in range(-1,3,2):  # -1 , 1 로 한번씩 시도
      
      if queue[0] in visited:  # 현상태가 


n, k = map(int,input().split())
li = list(map(int,input().split()))
li = sorted(li)
print(li)

count = 0 # 시행 횟수
while True:
  if li == li.sort():
    break
  count += 1



