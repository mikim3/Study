# 시작시간 0322 1423 마무리시간
# 못품
# "게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽~~" 끝난 뒤에 라는 말은 즉 그 시간에 수행할 코드를 모두 실행하고 방향을 회전하라는 의미이다.
# 지렁이 이동할때 머리는 append 꼬리는 popleft하는 테크닉 기억하기,  그리고 popleft한 값 그래프에 0으로 바꿔주기

from collections import deque

n = int(input())
k = int(input())
graph = [[0] * n for i in range(n)]
for i in range(k):
  row, col = map(int,input().split())
  graph[row - 1][col - 1] = 2
l = int(input())

queue = deque()
queue.append((0, 0))

dirDict = {}
for i in range(l):
  time, dir = map(str, input().split())
  dirDict[int(time)] = dir

dx = [0,1,0,-1] # 오, 아래, 왼쪽, 위
dy = [1,0,-1,0]
# 현재 바라보는 방향 오른, 아래, 왼쪽, 위
now_direction = 0
def turn(dir_turn):
  global now_direction
  if dir_turn == 'L':
    now_direction = (now_direction - 1) % 4
  if dir_turn == 'D':
    now_direction = (now_direction + 1) % 4

x, y = 0, 0
graph[x][y] = 1
# 현재 시간
time = 0

while True:
  time += 1
  x += dx[now_direction]
  y += dy[now_direction]
  if x < 0 or x >= n or y < 0 or y >= n:
    break
  if graph[x][y] == 2:
    graph[x][y] = 1
    queue.append((x,y))
    if time in dirDict:
      turn(dirDict[time])
  elif graph[x][y] == 0:
    graph[x][y] = 1
    queue.append((x, y))
    tx, ty = queue.popleft()
    graph[tx][ty] = 0
    if time in dirDict:
      turn(dirDict[time])
  else:
    break
print(time)

# # 시작시간 0321 1715 마무리시간
# # 못품

# from collections import deque

# n = int(input()) # 보드의 크기
# k = int(input()) # 사과의 개수

# graph = [[0] * n for _ in range(n)] # 보드를 0으로 초기화
# dx = [0, 1, 0, -1] # 동, 남, 서, 북 방향으로 x축 이동
# dy = [1, 0, -1, 0] # 동, 남, 서, 북 방향으로 y축 이동

# # 
# for i in range(k):
#   a, b = map(int, input().split())
#   graph[a - 1][b - 1] = 2
  
# l = int(input())
# dirDict = dict()
# queue = deque()
# queue.append((0,0))

# for i in range(l):
#   x,c = input().split()
#   dirDict[int(x)] = c

# x, y = 0, 0 
# graph[x][y] = 1
# count = 0
# direction = 0 # 뱀의 방향, 초기값은 동쪽

# # alpha == 'L', 'D' 방향을 뜻함
# def turn(alpha):
#   global direction
#   if alpha == 'L':
#     direction = (direction - 1) % 4 # 왼쪽으로 90도 회전
#   else:
#     direction = (direction + 1) % 4  # 오른쪽으로 90도 회전


# # 게임 진행 로직
# while True:
#   count += 1
#   x += dx[direction]
#   y += dy[direction]
  
#   # 벽에 부딪히면 게임 종료
#   if x < 0 or x >= n or y < 0 or y >= n:
#     break
  
#   # 사과를 만나면
#   if graph[x][y] == 2:
#     graph[x][y] = 1
#     queue.append((x, y))
#     if count in dirDict: # 방향 전환 할 시간이면
#       turn(dirDict[count])
    
#   # 빈 공간을 만나면
#   elif graph[x][y] == 0:
#     graph[x][y] = 1
#     queue.append((x, y))
#     tx, ty = queue.popleft()
#     graph[tx][ty] = 0
#     if count in dirDict:
#       turn(dirDict[count])
#   # 자기 자신의 몸과 부딪히면 게임 종료
#   else:
#     break
# print(count)
