# 시작시간 21:16

# 얼음이 상하좌우중에 갈수 있는곳을 찾아서 찾아간 길이들
# 중에 최고 길이를 출력

# import sys
# input = sys.stdin.readline
def dfs(x,y):
    # 벽을 넘으면 False
    if x <= -1 or x >= n or y <= -1 or y>=m:
        return False
    # 만약 구명이 뚤려있으면
    if graph[x][y] == 0:
        # 1로 체크를 한다.     
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x + 1,y)
        dfs(x,y + 1)
        return True
    return False

n,m = map(int,input().split())

# 2차원 배열
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
