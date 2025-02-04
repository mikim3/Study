# 시작시간 1758 마무리시간 1858
# 어떤 자료구조를 선택해야 될지를 생각하는 과정에서 시간을 많이 썼고
# 구현중 break범위를 착각해서 한번더 시간낭비

from collections import deque

n = int(input())
k = int(input()) # 사과의 개수

li =[[0] * n for _ in range(n)]  # map임
li[0][0] = 9  # 머리
now_head = (0,0) # 0,0에서 시작하고 오른쪽 보는중 
for i in range(k): # 사과의 위치
  x,y = map(int,input().split())
  li[x-1][y-1] = 1  # 사과

l = int(input())  # 방향정보 갯수
queue_dirction = deque()  # 방향정보
for i in range(l):
  x, c = input().split()  # 게임 시작부터 X초후 C방향 회전
  queue_dirction.append((int(x),c))

# 1 사과

# ->                           ^         
# 오른쪽(1) 다음은  L D 하면  L 위(0)  D 아래(2)  
# 위(0) 다음은 L D 하면 L 왼쪽(3) D 오른쪽(1)
# L -1 D +1   %4 한 나머지값 하면 되네

# 위, 오른쪽, 아래, 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
now_dirction = 1 # 오른쪽
time = 0
queue = deque() # 
queue.append(now_head)
finish_flag = 0
while True:
  # print("time,", time, "now_head", now_head, "now_dirction", now_dirction, "queue", queue)
  # 다음 머리 좌표
  next_x = now_head[0] + dx[now_dirction] 
  next_y = now_head[1] + dy[now_dirction] 
  if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n: # 맵밖으로감
    break # 게임끝
  # 몸이랑 만나면 끝
  if queue:
    for i in range(len(queue)):
      if queue[i] == (next_x, next_y):
        # print("hit my body")
        finish_flag = 1
        break # 이걸로는 안 끝나네 ㅠㅠ
    if finish_flag == 1:
      break
  # 사과인지 판별
  if li[next_x][next_y] == 1:
    queue.append((next_x, next_y))  # TODO 헷갈림
    li[next_x][next_y] = 0 # 사과 섭취
  else:
    queue.append((next_x, next_y))  # TODO 헷갈림
    queue.popleft() #꼬리 자르기
  now_head = (next_x, next_y)
  time += 1
  # 머리 돌리기
  if queue_dirction and queue_dirction[0][0] == time:
    if queue_dirction[0][1] == 'L':
      now_dirction = (now_dirction - 1) % 4   # -1 이면 3나옴
    if queue_dirction[0][1] == 'D': 
      now_dirction = (now_dirction + 1) % 4 
    queue_dirction.popleft()
    
print(time+1)
