# 시작시간 1722
"""

f(i,j) = min(f(i-1,j), f(i,j-1))

"""
def dfs(x,y):
  if dp[x][y] > 0:
    return dp[x][y]
  if x == 0 and y==0:
    return li[0][0]
  else:
    if y== 0:
      dp[x][y] = dfs(x-1,y) + li[x][y]
    elif x == 0:
      dp[x][y] = dfs(x,y-1) + li[x][y]
    else:
      dp[x][y] = min(dfs(x,y-1), dfs(x-1,y))+li[x][y]
    return dp[x][y]
n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
print(dfs(n-1,n-1))

# TopDown






