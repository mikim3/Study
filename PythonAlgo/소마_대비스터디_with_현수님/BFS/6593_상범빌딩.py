# 시작시간 1707 마무리시간 1741
# 새로운 아이디어로 다시 풀기 시작한 시간

# 생각해보니 2차원 형태로 생각하는데 z가 바뀔때를 x의 전체값 R 만큼을 한번에
# 순간이동 한다고 생각하면 훨씬 쉬워진다.

from collections import deque
import sys
input = sys.stdin.readline

# 특이하게 동서남북(4방향) + 상하(2방향) 6방향으로 움직임
# C는 가로  R은 줄의 갯수 그렇게 L번 주어진다.
#   "#"은 못지나감   비어있으면 '.'
# S에서 시작
# E는 출구
# 각층 사이에 빈줄
# L R C 가 모두 0 이면 종료

def bfs(li_building, start_vec):
  queue = deque()
  queue.append(start_vec)
  checked[start_vec[0]][start_vec[1]] = 1 # 시작위치 체크 z x y
  while queue:
    now = queue.popleft()
    # 층 옮기기
    # 층 안에서 움직이기
    for i in range(6):
      next_x = now[0] + dx[i]
      next_y = now[1] + dy[i]
      # 그래프 밖으로 벗어나면
      if next_x < 0 or next_x >= ((R + 1) * L) - 1 or next_y < 0 or next_y >= C or li_building[next_x][next_y] == 0:
        continue
      # 아직 안 갔지만 갈 수 있는 좌표
      if checked[next_x][next_y] == 0 and li_building[next_x][next_y] == '.':
        checked[next_x][next_y] = checked[now[0]][now[1]] + 1
        queue.append((next_x, next_y))
      elif li_building[next_x][next_y] == 'E':
        print("Escaped in",str(checked[now[0]][now[1]]),"minute(s).")
        return True
  return False

while True:
  L, R, C = map(int, input().strip().split())
  if L == 0 and R == 0 and C == 0:
    break
  dx = [-1, 0, 1, 0, R+1, -(R+1)] # 행 위아래
  dy = [0, 1, 0, -1, 0, 0] # 열 좌우
  checked = [[0] * C for _ in range(L * (R+1))]
  count_floor = 0 # 현재 층
  li_building = [] # 빌딩 리스트
  while count_floor < L:
    for i in range(R):
      li_building.append(list(input().strip()))
    list(input().strip())
    li_building.append([0] * C) # 층 사이 빈공간 채우기
    count_floor += 1
  for i in range(L * (R+1)):
    for j in range(C):
      if li_building[i][j] == 'S':
        if bfs(li_building, (i,j)) == False:
          print("Trapped!")
        break


# # 시작시간 1543 마무리시간
# # 빨리 풀수는 없어 보이는문제
# # 아이디어는 바로 떠올렸는데 어쩔수 없게 오래걸림

# # 생각해보니 2차원 형태로 생각하는데 z가 바뀔때를 x의 전체값 R 만큼을 한번에
# # 순간이동 한다고 생각하면 해결 됐을것 같다.

# from collections import deque
# import sys
# input = sys.stdin.readline

# # 특이하게 동서남북(4방향) + 상하(2방향) 6방향으로 움직임
# # C는 가로  R은 줄의 갯수 그렇게 L번 주어진다.
# #   "#"은 못지나감   비어있으면 '.'
# # S에서 시작
# # E는 출구
# # 각층 사이에 빈줄
# # L R C 가 모두 0 이면 종료

# def bfs(li_building, start_vec):
#   queue = deque()
#   queue.append(start_vec)
#   checked[start_vec[0]][start_vec[1]][start_vec[2]] = 1 # 시작위치 체크 z x y
#   while queue:
#     now = queue.popleft()
#     # 층 옮기기
#     for i in range(3):
#       next_z = now[0] + dz[i]
#       # 층 안에서 움직이기
#       for j in range(4):
#         next_x = now[1] + dx[j]
#         next_y = now[2] + dy[j]
#         # 그래프 밖으로 벗어나면
#         if next_x < 0 or next_x >= R or next_y < 0 or next_y >= C or next_z < 0 or next_z >= L:
#           continue
#         # 아직 안 갔지만 갈 수 있는 좌표
#         if checked[next_z][next_x][next_y] == 0 and li_building[next_z][next_x][next_y] == '.':
#           checked[next_z][next_x][next_y] = checked[now[0]][now[1]][now[2]] + 1
#           queue.append((next_z, next_x, next_y))
#         elif li_building[next_z][next_x][next_y] == 'E':
#           print("Escaped in",str(checked[now[0]][now[1]][now[2]] + 1),"minute(s).")
#           return True
#   return False
# dz = [0, 1, -1] # 층수 변화 0도 넣어야 되나????
# dx = [-1, 0, 1, 0] # 행 위아래
# dy = [0, 1, 0, -1] # 열 좌우

# while True:
#   L, R, C = map(int, input().strip().split())
#   if L == 0 and R == 0 and C == 0:
#     break
#   # 3차원 공간에 체크 만들기 0 이면 안 간 곳 값은 몇번 시도로 갔는지를 나타냄
#   checked = []
#   for i in range(L):
#     temp_checked = [[0] * C for _ in range(R)]
#     checked.append(temp_checked)
#   print(checked)
#   count_floor = 0 # 현재 층
#   li_building = [] # 빌딩 리스트
#   while count_floor < L:
#     temp_building_2cha = []
#     for i in range(R):
#       temp_building = list(input().strip())
#       temp_building_2cha.append(temp_building)
#     count_floor += 1
#     list(input().strip()) # 빈줄 흘리기
#     li_building.append(temp_building_2cha)
#   print(li_building)
#   # print('li_building',li_building[0][0][0])
#   # print('li_building',li_building[0][1][1])
#   # print('li_building',li_building[0][1][0])
#   # print('li_building',li_building[0][1][1])
#   # print('li_building',li_building[2][3][4])


#   # TODO : start 0,0,0 으로 일단 박음 귀찮다.  입력값에 맞게 고쳐야함
#   if bfs(li_building, (0,0,0)) == False:
#     print("Trapped!")

#   print(li_building)
