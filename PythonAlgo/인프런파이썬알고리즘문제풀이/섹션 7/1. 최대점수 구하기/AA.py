##############################
# 시작시간 240213 14:36 마무리시간 14:52
#
# def dfs(level):
#   global max_value
#   tmp_time = 0
#   for i in range(n):
#     if checked[i] == 1:
#       tmp_time += li_input[i][1]
#   if tmp_time > m:
#     return
#   if level >= n:
#     tmp = 0
#     for i in range(n):
#       if checked[i] == 1:
#         tmp += li_input[i][0]
#     if tmp > max_value:
#       max_value = tmp
#   else:
#     checked[level] = 1
#     dfs(level+1)
#     checked[level] = 0
#     dfs(level+1)
# # 점수, 걸리는 시간
# n, m = map(int ,input().split())
# li_input = []
# for i in range(n):
#   li_input.append(tuple(map(int,input().split())))
# checked = [0] * (n+1)
# max_value = 0
# dfs(0)
# print(max_value)

# ###############################
# # 시작시간 20:58 마무리시간 21:22

# #
# # 시간도 넘겨줘서 조기 종료 해보기
# def dfs(level, nowTime):
#   global high_score
#   if nowTime > m:
#     return
#   if level==n:
#     now_score = 0
#     for i in range(n):
#       if result[i] == 1:
#         now_score += li[i][0]
#     if now_score >= high_score:
#       high_score = now_score
#   else:
#     result[level] = 1
#     dfs(level+1,nowTime+li[level][1])
#     result[level] = 0
#     dfs(level+1, nowTime)

# n, m = map(int, input().split())
# li = []
# # 점수 시간 순 입력
# for i in range(n):
#   li.append(list(map(int, input().split())))
# print(li)
# count_time = 0
# high_score = 0
# result = [0] * (n)

# dfs(0, 0)
# print(high_score)




# # ##########################
# # # 시작시간 240101 00:05  마무리시간 00:48

# # def DFS(level):
# #   global max_value
# #   global now_time
# #   if now_time > m:
# #     return
# #   if level == n:
# #     tmp_result = 0
# #     for i in range(n):
# #       if check[i] == 1:
# #         tmp_result+=li[i][0]
# #     if max_value < tmp_result:
# #       max_value = tmp_result
# #   else:
# #     check[level] = 1
# #     now_time+= li[level][1]
# #     DFS(level+1)
# #     now_time-= li[level][1]
# #     check[level] = 0
# #     DFS(level+1)

# # n, m = map(int, input().split())
# # li= []
# # for i in range(n):
# #   li.append(list(map(int, input().split())))
# # # print(li)
# # # 해당 문제 풀었는지 저장
# # check= [0] * (n+1)
# # # result = [0] * (n+1)
# # # 현재 지난 시간
# # now_time = 0
# # max_value = 0
# # DFS(0)
# # print(max_value)
# # #########################
