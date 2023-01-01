# 시작시간 20:19

from collections import deque

def bfs(x, y):
    queue = deque()
    # 첫 좌표 (x,y) 형태로 저장
    queue.append((x,y))
    while queue:
        print(queue)
        # popleft면 처음 들어왔던 것 먼저 pop한다.
        x,y = queue.popleft()
        print("popleft after",queue)
        for i in range(4):
            # nx를 통해 다음 좌표를 비교할 수 있다.
            nx = x + dx[i]
            ny = y + dy[i]
            # 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 만약 다음 좌표가 1이면 즉 갈수 있다면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 도착지 주소값 반환
    return graph[n-1][m-1]
n , m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))
