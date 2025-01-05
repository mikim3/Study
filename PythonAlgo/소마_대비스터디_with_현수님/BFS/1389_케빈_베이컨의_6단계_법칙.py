# 시작시간 1250 마무리시간

# 단계들 총합

# 베이컨 가장 작은 사람 출력 겹치면 번호가 작은 사람 출력

# 1. 각자의 베이컨 수를 구한다. (베이컨 계산이 완전 BFS 다 )
# 2. 그 중 가장 적은 수를 구한다.

def bfs(graph, start_v):


n, m = map(int, input().split())
li = []
for i in range(m):
  li.append(int(input))  

# 최소베이컨 수
min_v = 99999999

graph = [[] for _ in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
# 각

