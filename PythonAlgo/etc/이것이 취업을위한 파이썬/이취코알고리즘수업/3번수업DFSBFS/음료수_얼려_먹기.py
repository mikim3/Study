
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우의 위치들도 모두 재귀적으로 호출
        # 상하좌우 재귀 호출을 하면 근처에 graph[x][y] == 0 인 부분은
        # 모두 방문처리가 된다.  그러다가 리스트 끝이나 1값을 만나면 거기서
        # 방문처리가 멈춘다.
        dfs(x - 1, y)
        dfs(x ,y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n,m = map(int,input().split())
# 2차원 리스트 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
print(graph)
# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS수행
        if dfs(i,j) == True:
            result += 1

print(result)  # 정답 출력
visited = [True] * (n*m+1)

