import sys

##############################
# 시작시간 240212 14:40 마무리시간
# 선생님이 알려준 풀이는 내가 모르는 공식이 있다.
# 못품

# def dfs(level, total):
#   if level == n and total == f:
#     for x in point:
#       print(x, end=' ')
#     print()
#     sys.exit()
#   else:
#     for i in range(1, n+1):
#       if checked[i] == 0:
#         checked[i] = 1
#         point[level] = i
#         dfs(level+1, total+(point[level] * multiple[level]))
#         checked[i] = 0

# n,f = map(int,input().split())

# # 해당 칸에 숫자가 총합에 몇번 계산되나
# point = [0] * n
# multiple = [1] * n
# checked = [0] *(n+1)
# # 조합 공식 같은거임
# for i in range(1,n):
#   multiple[i] = multiple[i-1] * (n-i) // i
# dfs(0,0)

# ##########################
# # 모법답안 라이브러리 사용하기
# # 코테에서 막을수도 있긴함
# # ~~조건만 만족하는 순열을 뽑으라고 하면 라이브러리로 안됨
# # 나는 걍 만들어 쓰는게 좋을듯

# import itertools as it

# n, f = map(int, input().split())
# b = [1] * n
# for i in range(1,n):
#   b[i] = b[i - 1] * (n - i)/i
# a = list(range(1, n + 1))
# for tmp in it.permutations(a):
#   sum = 0
#   for L,x in enumerate(tmp):
#     sum += (x * b[L])
#   if sum==f:
#     for x in tmp:
#       print(x, end=' ')
#     break


# ##########################
# # 시작시간 231226 20:01   마무리시간 20:06
# # 전에 푼거 복붙해서 다시 풀기
# # 하던중에 순열구하기 성능 더 좋은코드를 발견해서 그거 기준으로 만들기

# def make_soon_case(level):
#   if level == n:
#     if soon_case[0] != 0:
#       if f == calculator(soon_case):
#         for i in range(n):
#           print(soon_case[i], end=' ')
#         print()
#         sys.exit(0)
#   else:
#     for i in range(n):
#       if check[i] == 0:
#         check[i] = 1
#         soon_case[level] = i+1
#         make_soon_case(level + 1)
#         check[i] = 0

# def calculator(soon_case_param):
#   tmp = soon_case_param[:]
#   final_value = 0
#   for i in range(n - 1):
#     for j in range(n - i - 1):
#       tmp[j] = soon_case_param[j] + soon_case_param[j+1]
#     soon_case_param = tmp
#   final_value = soon_case_param[0]
#   return final_value
# # 순열 만들기
# n, f= map(int, input().split())
# # 몇번째 순열인지 카운트
# soon_case = [0] * (n)
# check= [0] * (n)
# level = 0

# make_soon_case(0)

# ##########################
# # 시작시간 231226 15:35   마무리시간 17:35
# # 3번, 5번 케이스에서만 시간 초과

# # 1부터 N까지의 수를 중복되지 않게 순서를 바꾸면서 나열하고
# # 그 나열된 값을 조건에 맞게 계산한다.

# # 순서를 바꾸면서 계산을 한다.

# # 순서를 바꿀때는 반드시 뒤에 위치한 값부터 바꿔야 된다.
# # 1 2 3 4,  1 2 4 3 둘다 답이면 1 2 3 4 를 선택

# # 계산은 그냥 무언가 다른 방법
# # 순서는 DFS맞음

# # li를 받아서 계산하는 함수 작성
# # 순서가 나오게끔 하는 함수 하나 만들기

# def make_soon_case(level):
#   global count
#   soon_case_sorted = sorted(soon_case)
#   if level == level_fin:
#     for i in range(0, n - 1):
#       if soon_case_sorted[i] == soon_case_sorted[i + 1]:
#         return
#     for i in range(n):
#       soon_cases[count][i] = soon_case[i]
#     if soon_cases[count][0] != 0:
#       if f == calculator(soon_cases[count]):
#         print('find right case')
#         print(soon_cases[count])
#         sys.exit(0)
#     count+=1
#   else:
#     for i in range(1, n + 1):
#       soon_case[level] = i
#       make_soon_case(level + 1)

# def calculator(soon_case_param):
#   tmp = soon_case_param[:]
#   tmp2 = soon_case_param[:]
#   final_value = 0
#   for i in range(n-1):
#     for j in range(n-i-1):
#       tmp[j] = soon_case_param[j] + soon_case_param[j+1]
#     soon_case_param = tmp
#   final_value = soon_case_param[0]
#   soon_case_param = tmp2
#   # print('cal final_value ==', final_value)
#   return final_value


# # 순열 만들기
# n, f= map(int, input().split())
# #
# level_fin = n
# #
# max_count_case = n**n
# # 순열 케이스를 모두 저장
# soon_cases = [[0] * n for _ in range(30000)]
# # soon_cases = [[0] * n for _ in range(max_count_case)]
# # 몇번째 순열인지 카운트
# count = 0
# #
# soon_case = [0] * (n)
# level = 0

# make_soon_case(0)
# # print('make soon_cases', soon_cases)

# # 나온 순열 계산하기
# su = [0] * (n+1)

# # print('len make_soon_case == ', len(soon_cases))

# # for i in range(len(soon_cases)):
# #   # 안 채워진 칸 발견
# #   if soon_cases[i][0] == 0:
# #     break
# #   if f == calculator(soon_cases[i]):
# #     print('find right case')
# #     print(soon_cases[i])
# #     break

# #########################













