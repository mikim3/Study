# 시작시간 1845 마무리시간 
# DFS로 풀어서 시간초과 났음
# 
import sys

result = 0

def dfs(num_pos, code_pos):
  global count 
  if num_pos >= m: # 코드끝까지 조합
    count += 1
    # for i in range(len(code)):
    #   print(code[i], end=' ')
    #   if code[i] == 0:
    #     break
    # print()
    # for i in range(len(code)):
    #   code[i] = 0 # 초기화
  else:
    for i in range(1,27): # 
      if i < 10: # 1의자리
        if num[num_pos] == i: # 1의 자리 일치
          code[code_pos] = i
          dfs(num_pos+1,code_pos+1)
          code[code_pos] = 0
      elif i >= 10: # 십의자리
        if num_pos < m-1 and num[num_pos] == i//10 and num[num_pos+1] == i % 10:
          code[code_pos] = i
          dfs(num_pos+2, code_pos+1)
          code[code_pos] = 0

# 입력 다시 생각해보기
num = list(map(int, input())) # 입력받은 숫자

m = len(num)
# visited = [0] * (m + 1)  # 사용한 숫자면 + 1
# [2,5,1,1,4,0], [25,1,1,4,0,0] , [2,5,11,4,0,0]  같은 값들 넣기
code = [0] * (m + 1)  # 
count = 0

finish_flag = 0
for i in range(m): # 암호 유효성 검사
  if not (num[i] >= 1 and num[i] <= 9):
    print(0)
    sys.exit()
dfs(0,0)
print(count%1000000)