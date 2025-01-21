# 시작시간 1719 마무리시간 1740
# DFS 망하고 다시 풀음
# 역순으로 하면  1,2행위를 하는 순서가 바로바로 판단이 가능해짐

# s를 1,2행위로 수행한 결과가 t이다.
# t를 리버스 1,2행위로 수행하면 s가 된다.

# 리버스 1,2행위
# 1. 문자열 뒤에 A를 제거한다.
# 2. B를 제거하고 문자열을 뒤집는다.

s = input()
t = input()
while len(t) > len(s):
  if t[-1] == 'A':
    t = t[:-1]
  elif t[-1] == 'B':
    t = t[:-1]
    t = t[::-1]
if t == s:
  print(1)
else:
  print(0)

# # 시작시간 1643 마무리시간
# # 얕은 복사 깊은 복사 잘 생각하기
# # DFS로 탐색하면
# # 2**n 시간 복잡도 인데 값 범위가 1000이니까 2**1000의 값이 나옴

# import sys

# def dfs(level):
#   if level == len_t:
#     tmp_word = li_s.copy()
#     # print('tmp_word', tmp_word)
#     for i in range(len_s, len_t):
#       if checked[i] == 1:
#         tmp_word.append('A')
#       elif checked[i] == 0:
#         tmp_word.reverse()
#         tmp_word.append('B')
#     # print('tmp_word',tmp_word, 'li_t', li_t)
#     if tmp_word == li_t:
#       print(1)
#       sys.exit()
#   else:
#     checked[level] = 1
#     dfs(level+1)
#     checked[level] = 0
#     dfs(level+1)
# s = input()
# t = input()
# li_s = list(s)
# li_t = list(t)
# len_s = len(s)
# len_t = len(t)
# checked = [0] * (len_t + 1) # 문자열에 무슨 변화 줄지 기록
# dfs(len_s)
# print(0) # 중간에 종료 안되면 못 찾은거임

