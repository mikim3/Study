##########################################
# 시작시간 231222 2225 마무리시간 2303

# 아이디어 1 
# 남아있는 얘들의 합이 너무 적으면 더이상 수행할 필요가 없다.
# -> NO한 애들의 합과 앞으로 남은 것들의 합이 지금까지 나온 값들의 최대보다 적으면 더 이상 볼 필요도 없다.
# max_value > YES + 아직안본애들

def DFS(node):
  global max_value
  if node >= n:
    su = 0
    for i in range(n):
      if ch[i] == 1:
        su += li[i]
    if max_value < su <= c:
      max_value = su
  else:
    su = 0
    for i in range(node):
      if ch[i] == 1:
        su+=li[i]
    for i in range(node,n):
      su += li[i]
    if su < max_value:
      return
    ch[node] = 1
    DFS(node + 1)
    ch[node] = 0
    DFS(node + 1)

li = []
c, n= map(int, input().split())
ch = [0] * (n+1)
for i in range(n):
  li.append(int(input()))
max_value = 0
DFS(0)

print(max_value)

#######################################
# # 시작시간  231006 16:22 마무리시간 16:40에 5 케이스만 스택 제한 걸린듯
# # 시간문제 해결을 위해 답봄

# # tsum  이미 판단을 시도한 지나간 노드들의 합을 말한다.
# # 이미 지나간걸 다 합친 것 보다 result값이 더 높다면 더 이상 계산할 필요가 없다.
# def dfs(level, currentSum, passedSum):
#   global result
#   # (total - passedSum) 남아 있는 더 계산해야할 것들의 합
#   # 현재값 + 남아있는 모두를 다 더해도 이미 나온  result보다 작다면 더 계산할 필요가 없다.
#   if currentSum + (total - passedSum) < result:
#     return
#   # 이른 종료조건
#   if currentSum > c:
#     return
#   # 종료조건
#   if level == n:
#     if currentSum > result:
#       result = currentSum
#   else:
#     dfs(level + 1, currentSum + badooks[level], passedSum + badooks[level])
#     dfs(level + 1, currentSum, passedSum + badooks[level])

# c, n = map(int , input().split())
# badooks = []
# for i in range(n):
#   badooks.append(int(input()))
# result = -2147000000
# total = sum(badooks)
# dfs(0, 0, 0)
# print(result)

#########################
