# 시작시간 :  240223 16:22   종료시간 :  
# 답봄

n = int(input())
li = list(map(int, input().split()))
seq = [0] * (n)
# i+1 이 지금 배치할려는 숫자
for i in range(n):
  skip = li[i]
  for j in range(n):
    # 자기보다 큰숫자의 공간 확보 and 들어갈 자리가 비어있음
    if skip == 0 and seq[j] == 0:
      seq[j] = i + 1
      break
    # 빈자리 발견
    elif seq[j] == 0:
      skip -= 1

for x in seq:
  print(x, end=' ')
  
# n = int(input())
# li = list(map(int, input().split()))
# li_result = [0] * (n)

# # 1부터 위치 정해주기
# for i in range(1,n+1):
#   skip = li[i-1]
#   pos = 0
#   flag = 0
#   while flag == 0:
#     if li[pos] != 0:
#       pos += 1
#     else:
#       break
#   while skip > 0:
#     if li_result[pos] == 0:
#       skip -= 1
#       pos += 1
#     else:
#       pos += 1
      
#   if li_result[pos] == 0:
#     li_result[pos + 1] = i
#   else:
#     while li_result[po]    
    