# 07:54 시작

# BFS과정
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 
# 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

from collections import deque
import queue

def bfs(graph,start,visited):
    # 큐 초기화
    queue = deque([start])
    # 
    visited[start] = True
    
    while queue:
        v = 
        
        for i in graph[v]:
            
            if not visited[v]:
                
                visited[v] = True




start = 1

visited = [False] * 9

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]


