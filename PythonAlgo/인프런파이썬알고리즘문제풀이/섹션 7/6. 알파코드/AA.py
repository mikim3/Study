from typing import List

#########################
# 시작시간
# 유형공부를 위해 다시품

# level : DFS 깊이   position : 문자열에 위치(code의 위치랑 다름)
def dfs(level, position):
  global count
  # 레벨까지 가서 문자열 완성
  if level == n:
    count += 1
    for j in range(position):
      print(chr(result[j]+ ord('A') - 1), end='')
    print()
  else:  # 가지 뻗는 코드
    for i in range(1, 27):
      if code[level] == i:
        result[position] = i
        # 일의자리 숫자
        dfs(level + 1, position + 1)
      elif i >= 10 and code[level] == i // 10 and code[level + 1] == i % 10:
        result[position] = i
        # 십의자리숫자여서 code기준 두자리를 사용했음
        dfs(level+2, position+1)

code = list(map(int, input()))
n = len(code)
code.insert(n, -1) # 인덱스 아웃 에러 안내는 테크닉
result = [0] * (n + 3)
count = 0
dfs(0, 0)
print(count)






# ###############################
# # 시작시간 16:13 마무리시간 16:52
# # 문제가 일부 기억 났지만 나만의 방법으로 품

# def dfs(level, tmp_li : List):
#   global count
#   if level == n:
#     for i in range(len(tmp_li)):
#       print(chr(tmp_li[i]+ord('A')-1), end='')
#     print()
#     count += 1
#   else:
#     # A~Z
#     for i in range(1,27):
#       if i < 10 and li[level] == i:
#         tmp_li.append(i)
#         tmp_tmp_li = tmp_li.copy()
#         dfs(level + 1, tmp_tmp_li)
#       elif i >= 10 and level + 1 < n and i // 10 == li[level] and i % 10 == li[level+1]:
#         tmp_li.pop()
#         tmp_li.append(i)
#         tmp_tmp_li = tmp_li.copy()
#         dfs(level + 2, tmp_tmp_li)

# li = list(map(int, input()))
# n = len(li)
# count = 0
# dfs(0,[])
# print(count)

# ###############################
# # 시작 시간 240111 22:00  마무리 시간 22:32
# # 문제가 너무 기억남

# def dfs(level, position):
#   if level == li_len:
#     for i in range(position):
#       print(chr(result[i]+ord('A')-1),end=' ')
#     print()
#   else:
#     for i in range(1,27):
#       if li[level] == i:
#         result[position] = i
#         dfs(level + 1, position + 1)
#       elif li[level] == i // 10 and li[level + 1] == (i % 10):
#         result[position] = i
#         dfs(level + 2, position + 1)

# li = list(map(int, input()))
# li_len = len(li)
# result = [0] * li_len
# print(li)
# dfs(0,0)


# ###########################
# # 시작시간 240106 17:20  마무리시간
# # 또 못품

# def DFS(level, position):
#   if level == li_len:
#     for i in range(position):
#       print(chr(result[i]+64), end=' ')
#     print()
#   else:
#     for i in range(1,27):
#       if li[level] == i:
#         result[position] = i
#         DFS(level+1,position+1)
#       elif i >= 10 and li[level] == i // 10 and li[level + 1] == i % 10:
#         result[position] = i
#         DFS(level + 2, position + 1)

# li = list(map(int,input()))
# li_len = len(li)
# print(li)
# result = [0] * (li_len)

# DFS(0,0)

# ############################
# # 240103 20분소요
# # 다시 혼자 작성
# def DFS(level, position):
#   global count
#   if level == code_len:
#     # print('result ==', result)
#     for i in range(position):
#       print(chr(result[i] + ord('A') - 1), end=' ')
#     print()
#     count+=1
#   else:
#     for i in range(1, 27):
#       if code[level] == i:
#         result[position] = i
#         DFS(level + 1, position + 1)
#       elif i >= 10 and code[level] == i//10 and code[level+1] == i%10:
#         result[position] = i
#         DFS(level+2, position + 1)

# code = list(map(int, input()))
# print(code)
# code_len = len(code)
# code.insert(code_len, -1)
# result = [0] * code_len
# count = 0
# DFS(0,0)
# print(count)

# #
# ##########################
# # 시작시간 18:35    마무리시간

# # 최대 길이 50
# # 반드시 조기종료 조건이 필요하다.

# # position은 출력될 문자의 위치를 나타냄
# def DFS(level, position):
#   global count
#   if level == n:
#     count +=1
#     for i in range(position):
#       print(chr(result[i]+64), end='')
#     print()
#   else:
#     for i in range(1, 27):
#       # 알파벳 일치하면
#       if code[level] == i:
#         result[position] = i
#         DFS(level + 1, position + 1)
#       # 두 자리수 일때       현재 level에 숫자가 10의 자리 역할 다음 level이 일에 자리수 역할
#       elif i >= 10 and code[level] == i//10 and code[level+1] == i % 10:
#         result[position] = i
#         DFS(level + 2, position + 1)

# # 1을 우선으로
# # 2를 후 순위로 바꿔주기
# code = list(map(int, input()))
# n = len(code)
# #
# code.insert(n, -1)
# result = [0] * (n+3)
# count = 0
# DFS(0, 0)
# print(count)
# #########################
