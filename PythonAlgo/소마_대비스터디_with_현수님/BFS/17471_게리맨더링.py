"""
시작시간 16:40

같은 지역구는 연결되어 있어야함

백트래킹으로 두개의 구역으로 분리
bfs로 구역내부를 순회

1. 구역나누기
  1. 한구역만 visited표시를 하고 아닌 곳이 나머지 구역이다.
2. 탐색


"""
from collections import deque

def bfs(area):
  q = deque()
  q.append(area[0])
  visited[area[0]] = 1
  count = 1 # 연결된 노드들의 갯수
  pop = person[area[0]] # 인구수
  while q:
    now = q.popleft()
    for next in injup[now]: #
      # 
      if visited[next] == 0 and next in area:
        count += 1
        pop += person[area[next]]
        visited[area[next]] = 1
        q.append(next)
  if count == len(area):
    return pop
  else:
    return -1
        
# 원하는 1구역의 갯수, 현재만든 갯수
def choose(one_len, count):
  global result
  if one_len == count:
    area1, area2 = [], []
    for i in range(len(visited)):
      if visited[i] == 0: # 1구역
        area1.append(i)
      else: # 2구역
        area2.append(i)
    a_pop, b_pop = bfs(area1), bfs(area2) # 인구수 반환
    if a_pop > 0 and b_pop > 0:
      result = min(result, abs(a_pop-b_pop))
    return 
  else:
    visited[count] = 1
    choose(one_len, count+1)
    visited[count] = 0


MAX = float('inf')
result = MAX
n = int(input())
person = list(map(int,input().split()))
injup = [[] for _ in range(n)]# 
# 인접한 지역구
for i in range(n):
  temp = deque(map(int,input().split()))
  temp.popleft()
  injup= list(temp)
print("injup")
for i in range(len(injup)):
  print(injup[i])
print()

# i 는 1구역의 갯수를 의미
for i in range(1,n//2+1):
  visited = [0] * n
  # 두구역 나누기
  choose(i,0)

if result == MAX:
  print(-1)
else:
  print(result)





# 시작시간 1043
"""
다시보기

x당 y 당 둘다 서로가 연결이 되어 있어야함

인구차이 최소로 하기
"""
# import sys
# from collections import deque

# MAX = float('inf')  # 결과 비교를 위한 최대값 설정
# input = sys.stdin.readline  
# N = int(input())  # 구역 개수 입력
# person = [0] + list(map(int, input().split()))  # 구역별 인구 수 리스트 (인덱스 1부터 시작)
# arr = [[] for _ in range(N+1)]  # 인접 구역 정보를 저장할 리스트

# # 인접 구역 정보 입력
# for i in range(1, N+1):
#   temp = deque(map(int, input().split()))
#   temp.popleft()  # 인접 구역 수 제거
#   arr[i] = list(temp)  # 인접 구역 번호 저장
# print(f'arr {arr}')

# def bfs(area):  # 구역 연결 여부 확인 및 인구 합계 계산
#   q = deque()
#   visited = [0] * (N+1)  # 방문 여부 체크 리스트
#   q.append(area[0])
#   visited[area[0]] = 1
#   temp = 0  # 인구 합계
#   count = 1  # 연결된 구역 수
#   while q:
#     node = q.popleft()
#     temp += person[node]
#     for nnode in arr[node]: # 인접 노드 탐색
#       if nnode in area and visited[nnode] == 0:  # 연결된 미방문 구역 탐색
#         visited[nnode] = 1
#         count += 1
#         q.append(nnode)
#   if count == len(area):  # 모든 구역이 연결된 경우
#     return temp
#   return None  # 연결되지 않은 경우

# # 구역을 두 그룹으로 나누는 백트래킹
# # n은 하고자 하는 그룹의 크기
# def choose(n, count):
#   global result
#   if count == n:  # 목표 구역 수 도달
#     area1, area2 = [], []
#     for i in range(1, N+1):
#       if visited[i] == 1:
#         area1.append(i)
#       else:
#         area2.append(i)
#     x, y = bfs(area1), bfs(area2)
#     if x is not None and y is not None:  # 두 구역 모두 유효하면
#       result = min(result, abs(x-y))
#     return
#   for i in range(1, N+1):
#     if visited[i] == 0:  # 선택되지 않은 구역
#       visited[i] = 1
#       choose(n, count+1)
#       visited[i] = 0  # 백트래킹

# # 메인 로직
# result = MAX
# for i in range(1, N // 2 + 1):  # 1부터 N/2까지 시도
#   visited = [0] * (N+1)
#   choose(i, 0)

# if result == MAX:  # 나눌 수 없는 경우
#   print(-1)
# else:  # 최솟값 출력
#   print(result)