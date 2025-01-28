# 시작시간 2334 마무리시간
# 답봄 어질어질 함

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit


# 최대한 많은 칸을 이동 해야함

# 작은 값에서 큰 값으로만 이동할 수 있다.

# 서로 연결된 메모리 제이션에 양쪽 값 모두에 +1 하면 될듯???  #


# 오히려 큰 값에서 작은 값으로 이동하는게 편할듯???
# 

# 탑 다운 메모리 제이션을 하자
# 메모리제이션을 하는데
# 만약에 다음 위치가 현재 


# 핵심 아이디어
# 14 -> 9  로 갔을때 

import sys
sys.setrecursionlimit(1000000)  # 파이썬 재귀 한도 늘리기
input = sys.stdin.readline  # 빠른 입력을 위해 readline 사용

n = int(input())  # 대나무 숲의 크기 n을 입력받음
li = [list(map(int, input().split())) for _ in range(n)]  # 대나무 숲의 정보를 2차원 리스트로 저장
dp = [[0]*n for _ in range(n)]  # 각 위치에서의 최대 이동 횟수 저장

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
  if dp[x][y]:  # 이미 방문하여 최댓값이 계산된 경우
    return dp[x][y]  # 저장된 값을 반환하여 중복 계산 방지

  dp[x][y] = 1 # 자기 자신 포함
  for i in range(4):
    n_x = x + dx[i]
    n_y = y + dy[i]

    if 0 <= n_x < n and 0 <= n_y < n:
      # 이동하려는 위치의 대나무 양이 현재 위치보다 많은 경우
      if li[n_x][n_y] < li[x][y]:
        # dp 업데이트: 현재 위치의 dp 값과 이동한 위치의 dp 값 + 1 중 큰 값을 선택
        dp[x][y] = max(dp[x][y], dfs(n_x, n_y) + 1)
  return dp[x][y]  # 현재 위치에서 시작하는 최장 경로 길이를 반환

result = 0  # 판다가 이동할 수 있는 칸의 수의 최댓값
for i in range(n):
    for j in range(n):
        # 각 위치에서 시작하여 이동할 수 있는 최대 칸 수를 계산하고, 그 중 최댓값을 갱신
        result = max(result, dfs(i, j))

print(result)  # 결과 출력