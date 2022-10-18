
from collections import deque


def bfs(graph,start,visited):
    # 시작 노드를 큐에 넣은 상태로 시작
    queue = deque([start])
    # 처음 부분 
    visited[start] = True
    # 큐가 다 pop할때까지 반복
    while queue:
        # 
        v = queue.popleft()
        print(v,end=' ')
        # graph[v]는 v노드와 연결된 노드를 의미
        for i in graph[v]:
            # 만약 i값이 방문하지 않은 노드라면
            if not visited[i]:
                # 큐에 추가
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
# graph노드 갯수 + 1 == 9
visited = [False] * 9
bfs(graph,1,visited)






