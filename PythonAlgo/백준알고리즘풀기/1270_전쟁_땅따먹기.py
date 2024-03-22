# 다른방법

from collections import defaultdict

n = int(input())
for i in range(n):
  dic = defaultdict(int)
  li = list(map(int, input().split()))
  total_num = li[0]
  
  # 숫자들의 등장 횟수 기록
  for j in range(1, total_num + 1):
    dic[li[j]] += 1
  
  flag = 0
  for num, count in dic.items():
    print('num', num, 'count', count)
    if count > total_num // 2:
      print(num)
      flag = 1
      break
  if flag == 0:
    print('SYJKGW')
  

# # 시작시간 0322 1700 마무리시간 17:13
# from collections import defaultdict

# n = int(input())
# for i in range(n):
#   dic = defaultdict(int)
#   li = list(map(int,input().split()))
#   total_num = li[0]
#   flag = 0
#   for j in range(1, total_num+1):
#     dic[li[j]] += 1
#     if dic[li[j]] > total_num // 2:
#       print(li[j])
#       flag = 1
#       break
#   if flag == 0:
#     print('SYJKGW')
