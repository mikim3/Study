# 시작시간 2300 마무리시간


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
N, M, K = map(int, input().split())
# 
li = []
graph = [(0,0,0,0,0) * N for _ in range(N)]  # 맵 

print(graph)
# 파볼 저장
for i in range(M):
  r,c,m,s,d = map(int,input().split())
  li.append((r,c,m,s,d))

# K번 명령
for i in range(K):
  pass
total = 0
for i in range(N):
  for j in range(N):
    total += graph[]
# 방향
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
