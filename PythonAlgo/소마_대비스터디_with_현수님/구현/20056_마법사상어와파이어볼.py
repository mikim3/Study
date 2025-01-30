# 시작시간 2300 마무리시간
import sys
input = sys.stdin.readline
import copy

# r행 c열 m질량 s속력 d방향
# 이동 후 질량 구하기

# 이동 명령 동작
# 1. d방향 s 이동
# 2.
#   1. 모두 하나로 합쳐짐
#   2. 4개의 파이어볼로 나누어짐
#   3. 나누어진 파볼
#     1. 질량은  합쳐진 파볼 질량합 /5  
#     2. 속력은 합쳐진 파볼 속력의합/ 합쳐진 파볼 개수
#     3. 합쳐지는 파볼 방향이 모두 홀수거나 모두 짝수면 방향 0,2,4,6  아니면 1,3,5,7
#   4. 질량이 0인 파볼 소멸 

# 맵크기, 파이어볼 갯수, 명령 횟수
N, M, K = map(int, input().strip().split())
# 입력 저장 리스트 
li = []
# 질량,속도,방향,갯수
graph = [[(0,0,0,0) for _ in range(N)] for _ in range(N)]  # 맵 
# 방향
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for i in range(N):
  print(graph[i])

# 파볼 저장
for i in range(M):
  r,c,m,s,d = map(int,input().strip().split())
  r -= 1
  c -= 1
  li.append((m,s,d))
  graph[r][c] = (m, s, d, 1)
for i in range(N):
  print(graph[i])

# K번 명령
for _ in range(K):
  # 질, 속, 방, 갯
  # 방향 
  # 0: 아직안옴 1: 이전이 홀수임 2: 이전이 짝수임 3: 홀짝 통일 실패
  tmp_graph = [[(0,0,0,0) for _ in range(N)] for _ in range(N)]  # 맵 
  for i in range(N):
    for j in range(N):
      if graph[i][j][2] > 0: # 파볼이 존재하는 칸이면
        # 이동
        nx = i + (dx[graph[i][j][2]] * graph[i][j][1])
        ny = j + (dy[graph[i][j][2]] * graph[i][j][1])
        tmp_graph[nx][ny][0] += graph[i][j][0] # 질
        tmp_graph[nx][ny][1] += graph[i][j][1] # 속
        
        # 방향 구하기
        if tmp_graph[nx][ny][2] == 0:
          if graph[i][j][2] % 2 == 0:
            tmp_graph[nx][ny][2] = 2
          else:
            tmp_graph[nx][ny][2] = 1
        elif tmp_graph[nx][ny][2] == 3:
          pass # 3이면 이미 방향 상관없어짐
        elif tmp_graph[nx][ny][2] == 1: # 지금까지 홀수임
          if graph[i][j][2] % 2 == 0: # 근데 짝수옴
            tmp_graph[nx][ny][2] = 3
        elif tmp_graph[nx][ny][2] == 2: # 지금까지 짝수임
          if graph[i][j][2] % 2 != 0: # 근데 짝수옴
            tmp_graph[nx][ny][2] = 3
        
        tmp_graph[nx][ny][3] += 1 # 갯
        
  tmp_graph2 = [[(0,0,0,0) for _ in range(N)] for _ in range(N)]  # 맵 
  for i in range(N):
    for j in range(N):
      # 나누기
      now_m = tmp_graph[i][j][0] // 5 
      if now_m == 0: # 질령 0이면
        tmp_graph[i][j] = (0,0,0,0) # 소멸
        continue
      now_s = tmp_graph[i][j][1] // tmp_graph[i][j][3]
      now_d = tmp_graph[i][j][2]
      if now_d == 3: # 방향 미 통일
        for z in range(1,9,2): # 1,3,5,7
          now_x = i + dx[z]
          now_y = j + dy[z]
      else: 
        for z in range(0,7,2): # 0,2,4,6
          now_x = i + dx[z]
          now_y = j + dy[z]
      
  # # 갯수를 하나로 만들기
  # for i in range(N):
  #   for j in range(N):
  graph = copy.deepcopy(tmp_graph2)  # 덮어쓰기

total = 0
for i in range(N):
  for j in range(N):
    total += graph[i][j][2]
    pass

