# 양방향 큐
from collections import deque

# 너비우선탐색
def bfs(graph, start, visited):
    # 큐에 시작할 노드 넣고 시작
    queue = deque([start])
    # 1번노드는 방문했다고 표시
    visited[start] = True
    # 큐를 다 pop해서 방문 안한 노드가 없을때까지 반복
    while queue:
        # 왼쪽부터 pop함으로써 큐처럼 사용
        v = queue.popleft()
        print(v, end=' ')
        # graph에서 해당 노드와 인접한 노드 탐색  graph[1] == [2,3,8]
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True 
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
# 방문 여부 초기화
visited = [False] * 9
# 
bfs(graph, 1, visited)
