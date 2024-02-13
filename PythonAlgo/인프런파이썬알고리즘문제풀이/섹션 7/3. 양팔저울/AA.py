##########################
# 시직시간 240213 16:58  마무리시간 17:09

def dfs(level):
  if level == k:
    tmp = 0
    for i in range(k):
      if checked[i] == 2:
        tmp += li[i]
      elif checked[i] == 1:
        tmp -= li[i]
    if tmp > 0:
      set_value.add(tmp)
  else:
    checked[level] = 2
    dfs(level+1)
    checked[level] = 1
    dfs(level+1)
    checked[level] = 0
    dfs(level+1)

k = int(input())
li = list(map(int, input().split()))
checked = [0] * (k+1)
set_value= set()
dfs(0)
print(set_value)
print(sum(li)- len(set_value))


##########################
# 시작시간  18:57   마무리시간 19:28

# def DFS(level):
#   if level == n:
#     # 임시로 계산된 값
#     tmp_cal_value = 0
#     for i in range(n):
#       if check[i] == 2:
#         tmp_cal_value += li[i]
#       elif check[i] == 1:
#         tmp_cal_value -= li[i]
#     if 0 < tmp_cal_value < s+1:
#       check_can_value[tmp_cal_value] = 1
#   else:
#     check[level] = 2
#     DFS(level + 1)
#     check[level] = 1
#     DFS(level + 1)
#     check[level] = 0
#     DFS(level + 1)

# n = int(input())
# li = list(map(int, input().split()))
# s= sum(li)
# # 2더할지 1뺄지 0계산 안 할지
# check = [0] * n
# # 나올수 있는 값인지 확인 1 ~ s까지 확인
# check_can_value = [0] * (s+1)
# count = 0
# DFS(0)
# for i in range(1,s + 1):
#   if check_can_value[i] == 0:
#     count += 1
# print(count)
#########################
