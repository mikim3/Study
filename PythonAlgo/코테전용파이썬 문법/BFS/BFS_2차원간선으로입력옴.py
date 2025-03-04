from collections import defaultdict, deque

def bfs(graph, start_v):
  visited = [start_v]

def solution(edges):
  # 인접 리스트로 그래프 구성
  graph  = defaultdict(list)
  for li in edges:
    print(li)
    graph[li[0]].append(li[1])
    graph[li[1]].append(li[0])
  print(graph)
  
# 간선리스트
edges1 = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
edges2 = [[1,2],[2,3],[3,4]]
edges3 = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

print('111111111111\n', solution(edges1))
print('222222222\n', solution(edges2))
print('3333333333\n', solution(edges3))




