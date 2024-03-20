# 시작시간 0320 1823 마무리시간 1839
# dfs(depth+1, idx+1) 로 또 틀림

def dfs(depth, idx):
  global min_diff
  if depth >= n//2:
    team1, team2 = 0, 0
    for i in range(n):
      for j in range(n):
        if visited[i] and visited[j]:
          team1 += li[i][j]
        elif not visited[i] and not visited[j]:
          team2 += li[i][j]
    min_diff = min(min_diff, abs(team1 - team2))
    return
  else:
    for i in range(idx, n):
      if not visited[i]:
        visited[i] = 1
        dfs(depth+1, i+1) # 이거 또 틀림
        visited[i] = 0
n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
min_diff = 999999
dfs(0,0)
print(min_diff)

# # 시작시간 0320 16:19 마무리시간
# # 답봄
# # 뭔가 이해는 가는데 헷갈리고 다시보면 못풀듯
# #  depth는 현재 선택된 팀원 수, idx는 탐색을 시작할 인덱스
# def dfs(depth, idx):
#   global min_diff
#   if depth == n // 2:
#     power1, power2 = 0, 0
#     for i in range(n):
#       for j in range(n):
#         if visited[i] and visited[j]: # 둘 다 선택된 팀원이면 첫 번째 팀의 능력치에 더함
#           power1 += li[i][j]
#         elif not visited[i] and not visited[j]: # 둘 다 선택되지 않은 팀원이면 두 번째 팀의 능력치에 더함
#           power2 += li[i][j]
#     min_diff = min(min_diff, abs(power1 - power2))
#     return
#   for i in range(idx, n):
#     if not visited[i]:# 아직 선택되지 않은 사람이라면
#       visited[i] = 1 # 선택되었다고 표시
#       dfs(depth+1, i+1) # 다음 깊이로 탐색을 계속하며, 다음 사람부터 탐색을 시작
#       visited[i] = 0 # 백트래킹: 탐색이 끝난 후, 다시 선택되지 않은 상태로 되돌림

# li = []
# n = int(input())
# for i in range(n):
#   li.append(list(map(int,input().split())))
# visited = [0 for _ in range(n)]
# min_diff = 999999

# dfs(0,0)
# print(min_diff)
