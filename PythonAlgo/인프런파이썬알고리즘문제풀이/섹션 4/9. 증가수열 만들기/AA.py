# 260214 시작 1947  마무리 2020

# 왼쪽 오른쪽 중에 작은거 골라야 유리함
n = int(input())
li = list(map(int,input().split()))
li_res = []
lt=0
rt=n-1
last_num = 0
while lt <= rt:
  if li[lt] < li[rt]: #
    if last_num < li[lt]:
      li_res.append("L")
      last_num = li[lt]
      lt+=1
    else:
      if last_num < li[rt]:
        li_res.append("R")
        last_num = li[rt]
        rt-=1
      else:
        break
  else:
    if last_num < li[rt]:
      li_res.append("R")
      last_num = li[rt]
      rt-=1
    else:
      if last_num < li[lt]:
        li_res.append("L")
        last_num = li[lt]
        lt+=1
      else:
        break
print(len(li_res))
for i in range(len(li_res)):
  print(li_res[i],end='')
print()

# 시작시간 :  240223 1550  종료시간 :  


# n = int(input())
# li = list(map(int, input().split()))
# li_LR = []
# # 숫자쌓기 2 3 4 5 
# li_result = []

# if li[0] > li[-1]:
#   li_result.append(li.pop())
#   li_LR.append('R')
# else:
#   li_result.append(li.pop(0))
#   li_LR.append('L')
# while li:
#   #오른쪽이 더 작음 오른쪽 선호
#   if li[0] > li[-1]:
#     # 오른쪽 쓸수 있음
#     if li[-1] > li_result[-1]:
#       li_result.append(li.pop())
#       li_LR.append('R')
#     # 오른쪽 못씀 왼쪽 쓰기
#     if li[0] > li_result[-1]:
#       li_result.append(li.pop(0))
#       li_LR.append('L')
#     # 왼오 둘다 못씀
#     else:
#       break
#   else:
#     # 오른쪽 못씀 왼쪽 쓰기
#     if li[0] > li_result[-1]:
#       li_result.append(li.pop(0))
#       li_LR.append('L')
#     # 오른쪽 쓸수 있음
#     if li[-1] > li_result[-1]:
#       li_result.append(li.pop())
#       li_LR.append('R')
#     # 왼오 둘다 못씀
#     else:
#       break

# print(len(li_LR))
# for i in range(len(li_LR)):
#   print(li_LR[i], end='')
