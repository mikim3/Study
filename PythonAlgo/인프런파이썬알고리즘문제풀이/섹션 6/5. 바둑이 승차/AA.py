#######################################
# 시작시간  231006 16:22 마무리시간 16:40에 5 케이스만 스택 제한 걸린듯
# 시간문제는 해결못함

# tsum  이미 판단을 시도한 지나간 노드들의 합을 말한다.
# 이미 지나간걸 다 합친 것 보다 result값이 더 높다면 더 이상 계산할 필요가 없다.
def dfs(level, currentSum, passedSum):
  global result
  # (total - passedSum) 남아 있는 더 계산해야할 것들의 합
  # 현재값 + 남아있는 모두를 다 더해도 이미 나온  result보다 작다면 더 계산할 필요가 없다.
  if currentSum + (total - passedSum) < result:
    return
  # 이른 종료조건
  if currentSum > c:
    return
  # 종료조건
  if level == n:
    if currentSum > result:
      result = currentSum
  else:
    dfs(level + 1, currentSum + badooks[level], passedSum + badooks[level])
    dfs(level + 1, currentSum, passedSum + badooks[level])

c, n = map(int , input().split())
badooks = []
for i in range(n):
  badooks.append(int(input()))
result = -2147000000
total = sum(badooks)
dfs(0, 0, 0)
print(result)

#########################
