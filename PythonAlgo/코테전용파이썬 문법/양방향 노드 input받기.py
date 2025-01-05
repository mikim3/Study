from collections import deque

def bfs(graph, start_v):
    
  pass

n, m = map(int ,input().split())

graph = [[] for _ in range(n)]

for i in range(m):
  a, b = map(int , input().split())
  graph[a].append(b)
  graph[b].append(a)
start, end = map(int, input().split())



#################################
## 입력 예시
# 5 4  # 벡터 갯수 간선 갯수
# 1 3  # 서로 이어진 경로들(양방향)
# 2 3
# 4 3
# 5 1
# 5 4  # 5 -> 4 까지 가는 최단 경로



