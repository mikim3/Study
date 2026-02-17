# 260216 시작 1858  마무리 1930
from collections import deque

req = deque(input())
# print(req)
n = int(input())
for i in range(n):
  flag = "YES" # YES
  req_t = req.copy()
  se = deque(input())
  for j in range(len(se)):
    if req_t:
      if se[j] in req_t:
        if se[j] == req_t[0]:
          req_t.popleft()
        else:
          flag="NO"
          break
  if len(req_t) != 0:
    flag = "NO"
    # print(req_t)
  print(f"#{i+1}",flag)

##########################
# 시작시간 230929 14:18    마무리시간 14:51
# 문법적으로 더 쉬운 방법이 있을꺼라는 예상은 들지만 일단 되는데로 풀음

# required_str = input()
# required = list()
# for x in required_str:
#   required.append(x)
# n = int(input())

# for i in range(n):
#   required_tmp = required.copy()
#   tmp = input()
#   li = []
#   for x in tmp:
#     li.append(x)
#   j = 0
#   while li:
#     # 필수과목 안에 있으면
#     if li[j] in required_tmp:
#       if li[j] == required_tmp[0]:
#         required_tmp.remove(li[0])
#         li.remove(li[j])
#       else:
#         print(f"#{i+1} NO")
#         break
#     else:
#       li.remove(li[j])
#     if li == []:
#       if required_tmp == []:
#         print(f"#{i+1} YES")
#       else:
#         print(f"#{i+1} NO")
      
#########################
