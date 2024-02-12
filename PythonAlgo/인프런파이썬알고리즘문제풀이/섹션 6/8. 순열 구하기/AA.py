###########################
# 시작시간 240212 0809 마무리시간 0850
# 어쩌다 풀기는 했는데 이해가 덜 되었음

# def dfs(level):
#   global count
#   if level >= m:
#     count += 1
#     for i in range(m):
#       print(result[i],end=' ')
#     print()
#   else:
#     for i in range(1, n+1):
#       if checked[i] == 1:
#         continue
#       checked[i] = 1
#       result[level] = i
#       dfs(level+1)
#       checked[i] = 0
  
# n,m = map(int,input().split())
# checked = [0] * (n+1)
# result = [0] * (n+1)
# count = 0
# dfs(0)  
# print(count)


# #####################
# # 시작시간 231226 2117 마무리시간 231226 2124

# def DFS(level):
#   global count
#   if level == m:
#     for i in range(m):
#       print(result[i], end=' ')
#     print()
#   else:
#     for i in range(n):
#       if check[i] == 0:
#         check[i] = 1
#         result[level] = i+1
#         DFS(level + 1)
#         check[i] = 0

# n, m = map(int,input().split())
# # i번째항이 1 이면 i 번째항을 사용했다는 뜻
# check = [0] * n
# # i번째항이 3이면 i번째로 선택된 숫자는 3
# result = [0] * m
# count = 0
# DFS(0)

# ####################
# # 모범답안 근데 10,10 이면 이것도 마찬가지로 시간초과임
# # 그래도 이게 최선으로 빠름

# # def DFS(level):
# #   global count
# #   if level == m:
# #     for j in range(level):
# #       print(result[j], end=' ')
# #     print()
# #     count+=1
# #   else:
# #     for i in range(1, n + 1):
# #       if ch[i] == 0:
# #         # 체크하고 값 result에 넣고 다음 레벨로 넘어감
# #         ch[i] = 1
# #         result[level] = i
# #         DFS(level + 1)
# #         ch[i] = 0 # 리스트에서 level이 위로 올라간 상황이 표현됨

# # n, m = map(int, input().split())
# # # 현재 만드는 중인 리스트
# # result = [0] * n
# # # 지금 만드는 중인 리스트가 i 번째 인덱스를 사용했는지 check
# # # 그러기 때문에 ch[i] == 1 이면 i를 쓴다는 뜻
# # ch = [0] * (n + 1)
# # count = 0
# # DFS(0)
# # print(count)

# # ################################
# # # 시작시간 22:46 마무리시간 23:02
# # # 알고보니 시간 복잡도 문제 있었음
# # # 재도전

# # def DFS(level):
# #   global count
# #   if level == m:
# #     li_sorted = sorted(li)
# #     for i in range(m-1):
# #       if li_sorted[i] != 0 and li_sorted[i] == li_sorted[i+1]:
# #         return
# #     for i in range(m):
# #       print(li[i], end=' ')
# #     print()
# #     count+=1
# #   else:
# #     for i in range(1, n+1):
# #       li[level] = i
# #       DFS(level+1)
# # n, m = map(int, input().split())
# # li = [0] * (m)
# # count = 0
# # DFS(0)
# # print(count)

# # ##########################
# # # 시작시간 231224 15:55    마무리시간 1627
# # # 전에 풀었던 중복순열 구하기를 봐서 풀수 있었음 다시풀기

# # #
# # def DFS(level):
# #   global count
# #   if level == m:
# #     result_sorted = sorted(result)
# #     # print("result == ",result)
# #     # print("result_sorted == ",result_sorted)
# #     for i in range(n):
# #       if result_sorted[i] != 0:
# #         if result_sorted[i] == result_sorted[i+1]:
# #           return
# #     for i in range(m):
# #       print(result[i], end=' ')
# #     print()
# #     count+=1
# #   else:
# #     for i in range(1,n+1):
# #       result[level] = i
# #       DFS(level + 1)

# # count = 0
# # n, m = map(int, input().split())
# # result = [0] * (n+1)

# # DFS(0)
# # print(count)

# # #########################
