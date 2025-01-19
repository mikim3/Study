# 시작시간 마무리시간
# 한 거리씩 판단하는 테크닉 생각 오래걸림

from collections import deque

# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(checked, shark_size, start_pos):
  global shark_x
  global shark_y
  queue = deque()
  queue.append(start_pos)
  # 시작점을 방문 처리(거리 1로 설정)
  checked[start_pos[0]][start_pos[1]] = 1

  flag = 0  # 먹을 물고기를 찾았는지 여부 (0: 못찾음, 1: 찾음)

  while queue:
    size = len(queue)
    # 한 "거리 레벨"씩 탐색
    for _ in range(size):
      now = queue.popleft()
      for i in range(4):
        next_x = now[0] + dx[i]
        next_y = now[1] + dy[i]

        # 범위 밖은 무시
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
          continue
        # 상어보다 큰 물고기는 못 지나감
        if li[next_x][next_y] > shark_size:
          continue
        
        # 다음 칸까지의 거리 계산 (현재 거리 + 1)
        next_dist = checked[now[0]][now[1]] + 1

        # 아직 방문 안 했거나, 더 짧은 거리로 갱신 가능하면
        if checked[next_x][next_y] == 0 or checked[next_x][next_y] > next_dist:
          checked[next_x][next_y] = next_dist
            
          # 먹을 수 있는 물고기라면 (0보다 크고, 상어 사이즈보다 작음)
          if 0 < li[next_x][next_y] < shark_size:
            # 거리, 좌표를 li_dest_case에 추가
            li_dest_case.append((checked[now[0]][now[1]], next_x, next_y))
            flag = 1
          queue.append((next_x, next_y))
    
    # 이번 거리 레벨에서 먹을 수 있는 물고기가 하나라도 발견됐다면,
    # 더 이상 먼 거리까지 BFS를 진행하지 않고 종료
    if flag == 1:
        break

  return flag  # 1이면 물고기 찾음, 0이면 찾지 못함

n = int(input())
shark_size = 2 # 상어 크기
li = [] # 공간
li_dest_case = []
count = 0 # 이동 횟수 (결과적으로 출력할 시간)

for i in range(n):
    li.append(list(map(int, input().split())))

shark_eat = 0
shark_x, shark_y = -1, -1

# 상어의 초기 위치 찾기
for i in range(n):
    for j in range(n):
        if li[i][j] == 9:
            shark_x, shark_y = i, j

while True:
  # 매번 BFS를 위해 checked 배열 초기화
  checked = [[0]*n for _ in range(n)]
  move_flag = bfs(checked, shark_size, (shark_x, shark_y))

  # move_flag가 0이면 먹을 물고기 없음 -> 종료
  if move_flag == 0:
    break
  else:
    # BFS 중에 찾은 물고기가 있다면, 여러 마리를 li_dest_case에 담아두었음
    # (거리, x, y) 형태 -> 문제 조건(거리 같으면 위/왼쪽) 순으로 정렬
    # 기본 sort() -> (첫 번째 -> 두 번째 -> 세 번째 요소) 순서대로 오름차순
    li_dest_case.sort()

    # 가장 가까우면서, 위/왼쪽에 있는 물고기 선택
    select = li_dest_case[0]

    # 상어가 있던 자리는 0으로 만듦
    li[shark_x][shark_y] = 0

    # 이동 거리(= select[0])만큼 시간 누적
    count += select[0]

    # 상어 위치 갱신
    shark_x, shark_y = select[1], select[2]
    shark_eat += 1

    # 상어가 자신의 크기만큼 물고기를 먹으면 크기 1 증가
    if shark_eat >= shark_size:
      shark_size += 1
      shark_eat = 0

  # li_dest_case 초기화
  li_dest_case = []

# 최종 시간 출력
print(count)

# # 시작시간     마무리시간
# from collections import deque
# import sys

# input = sys.stdin.readline
# # 자기보다 작은애만 먹을수 있음
# # 
# # 자기보다 큰 물고기 있는 칸 지나가기 X
# # 자기보다 작은 물고기만 섭취
# # 자기랑 크기 같은놈은 지나가기 가능
# # 먹을수 있는 물고기 없음 끝
# # 거리가 가장 가까운 물고기를 먼저 먹으러감
# #   가장위를 우선  그 다음 가장 왼쪽 우선

# # 이동을 보내면서 조건 확인해서 가장 가까운 놈 먼저 먹기


# # 반환할떄 이동완료할 수 있는 목적지를 모두 배열에 추가하고 배열에서 가장 조건에 맞는 값 추가
# # 출발지에서 목적지까지 최단거리
# # 이동 완료하고 이동거리 카운트해야지 길에 막혀 못가는 경우에 카운트 안됨 
# def bfs(checked,shark_size, start_pos):
#   global shark_x
#   global shark_y
#   queue = deque()
#   queue.append(start_pos)
#   checked[start_pos[0]][start_pos[1]] = 1 # 시작점 체크
#   flag = 0 # 0으로 유지되면 굶은거임
#   while queue:
#     now = queue.popleft()
#     for i in range(4):
#       next_x = now[0] + dx[i]
#       next_y = now[1] + dy[i]

#       if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
#         continue
#       if li[next_x][next_y] > shark_size:
#         continue
#       elif li[next_x][next_y] == shark_size or li[next_x][next_y] == 0: # 그냥 지나가기
#         if checked[next_x][next_y] > checked[now[0]][now[1]] + 1 or checked[next_x][next_y] == 0:
#           checked[next_x][next_y] = checked[now[0]][now[1]] + 1
#           queue.append((next_x,next_y))
#       else: # 상어 사이즈가 더 작으면 먹기
#         # 현재 x y 값 도착하는데 비용 checked~ 만큼 든다.
#         li_dest_case.append((checked[now[0]][now[1]],next_x, next_y))
#         flag = 1
#   return flag

# # 위, 왼, 아,오   # 이렇게 하는게 영향 있나???
# dx = [-1,0,1,0]
# dy = [0,-1,0,1]
# n = int(input().strip())
# shark_size = 2 # 상어 크기 
# li = []  # 입력값 배열
# li_dest_case = [] # 목적지 도착한
# count = 0 # 이동 횟수
# for i in range(n):
#   li.append(list(map(int,input().strip().split())))
# shark_eat = 0
# # 상어 위치
# shark_x,shark_y = -1,-1
# for i in range(n):
#   for j in range(n):
#     if li[i][j] == 9:
#       shark_x, shark_y = i, j
# while True:
#   checked = [[0] * n for _ in range(n)] # 안 간 곳은 0 나머지는 거리값
#   move_flag = bfs(checked, shark_size, (shark_x,shark_y))
#   if move_flag == 0: # 길 막힘
#     break
#   else:
#     shark_eat += 1
#     # [(이동거리, x, y), (...)]  값으로 들어있음
#     # li_dest_case.sort(key=lambda x : (x[0], x[1], x[2]))
#     li_dest_case.sort()
#     select = li_dest_case[0]  # 선택된 이동거리, 갈x, 갈 y
#     li[shark_x][shark_y] = 0 # 기존 상어위치 먹어서 사라짐
#     li[select[1]][select[2]] = 9 # 상어이동
#     count += select[0]
#     shark_x, shark_y = select[1], select[2]
#   if shark_eat >= shark_size: # 사이즈업
#     shark_size+=1
#     shark_eat = 0
#   li_dest_case = [] # 배열 초기화

# print(count)
