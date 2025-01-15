# 시작시간 1508 마무리시간 1535
# 바로 풀었는데 반례를 찾느라 좀 더 걸렸음
# 모든 수열을 체크하지 않아서 아무값도 더하기 안하고 그래서 값이 0이 나오는경우를 늦게 떠올림

# 문제 조건에 N 최대 20개
# DFS로 해결

# # 몇 번째 숫자를 쓸지 말지를 결정하는 DFS 코드로 풀면 됨

def dfs(level):
  global sum_value
  global count
  if level >= n:
    if sum_value == s:
      count += 1
      li_sum_value.append(sum_value)
  else:
    sum_value += li[level]
    dfs(level+1)
    sum_value -= li[level]
    dfs(level+1)

n, s = map(int, input().split())
li = list(map(int, input().split()))

sum_value = 0
count = 0
li_sum_value = []

dfs(0)
if s == 0:
  count -= 1
print(count)

##############################
# 같은날 위에 코드가 틀린줄 알고 한번 더 다른 코드로 풀었음
# 개수가 최대 20개
# DFS로 해결

# 몇 번째 숫자를 쓸지 말지를 결정하는 DFS 코드로 풀면 됨
# def dfs(level):
#   global count
#   if level >= n:
#     sum_value = 0
#     for i in range(level):
#       if checked[i] == 1:
#         # print(li[i], end=' ')
#         sum_value += li[i]
#     if sum_value == s:
#       # print('findddd')
#       # if checked[i] == 1: ##########
#       #   print(li[i], end=' ')
#       count += 1
#     # print()
#   else:
#     checked[level] = 1
#     dfs(level+1)
#     checked[level] = 0
#     dfs(level+1)

# n, s = map(int, input().split())
# li = list(map(int, input().split()))

# # sum_value = 0
# count = 0
# checked = [0] * (n + 1)

# dfs(0)
# if s == 0:
#   count -= 1
# print(count)

# # 시작시간 1508 마무리시간

