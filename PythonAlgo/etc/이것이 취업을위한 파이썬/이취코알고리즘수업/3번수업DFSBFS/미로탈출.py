# 시작시간 09:44

from collections import deque
import queue
# 동빈이는 1,1에서 시작  출구는 n,m 

def bfs(x,y):
    queue = deque()
    # 시작 위치 큐에 추가
    queue.append((x,y))

    while queue:
        print(queue)
        # 가장 초반에 들어온 좌표
        x, y = queue.popleft()
        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                # print("graph[nx,ny] == 1")
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

# 
n,m = map(int,input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))
