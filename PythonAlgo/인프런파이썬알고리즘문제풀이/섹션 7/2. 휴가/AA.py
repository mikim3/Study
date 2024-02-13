############################
# 시작시간 240213 15:20 마무리시간 16:56
# 그냥 다시 풀면 빨리 풀었을텐데 내가 틀린이유를 찾느라 1시간 넘게씀

# 5일에 2일치하면 7일부터 일가능
# 1일에 4일치하면 5일부터 일가능
# 7일에 1일치하면 8일부터 일가능

# t걸리는날짜 p 보수비용

# 레벨,  일하는중(남은시간)
def dfs(level):
  global max_value
  if level > n:
    return
  if level == n:
    tmp = 0
    for i in range(n):
      if checked[i] == 1:
        tmp+= li_input[i][1]
    if tmp > max_value:
      max_value = tmp
  else:
    checked[level] = 1
    dfs(level + li_input[level][0])
    checked[level] = 0
    dfs(level+1)
n = int(input())
li_input = []
for i in range(n):
  li_input.append(tuple(map(int, input().split())))
checked = [0] * (n)
max_value = 0
dfs(0)
print(max_value)

##########################
# 시작시간 16:45 마무리시간 17:40

# # n일 까지만 일 할수 있다.
# # 최대 값이 나올수 있는 부분집합
# def DFS(level, remain_work):
#   # global total
#   global max_su
#   if level == n:
#     if remain_work > 0:
#       return
#     now_time = 0
#     tmp_su = 0
#     for i in range(n):
#       if check[i] == 1:
#         now_time += li[i][0]
#     if now_time <= n:
#       for i in range(n):
#         if check[i] == 1:
#           tmp_su+=li[i][1]
#       if tmp_su > max_su:
#         max_su = tmp_su
#   else:
#     check[level] = 1
#     if remain_work == 0:
#       DFS(level + 1, li[level][0] - 1)
#     check[level] = 0
#     if remain_work > 0:
#       remain_work -= 1
#     DFS(level + 1, remain_work)

# n = int(input())
# li = []
# for i in range(n):
#   li.append(list(map(int,input().split())))
# check = [0] * (n)
# max_su = 0
# DFS(0, 0)
# print(max_su)
#########################
