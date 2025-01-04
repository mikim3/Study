# 시작시간 20:42  마무리 시간
# 답봄
# 개념은 이해 되지만 너무 헷갈림
# 꼭 다시 보자


# +는 push
# - 는 pop

# 기본적으로 push를 하다가 만약에 현재 인덱스 부분에 수랑 최근에 들어온 수가 일치하면 pop

import sys 
input = sys.stdin.readline

n = int(input())
li_in = []
li_p_m = []
y_n = True

now = 1
stack = []
for i in range(n):
  #
  in_num = int(input())
  #
  while now <= in_num:
    stack.append(now)
    li_p_m.append('+')
    now += 1
    
  if stack[-1] == in_num:
    li_p_m.append('-')
    stack.pop()
  else:
    y_n = False

if y_n == True:
  for i in range(len(li_p_m)):
    print(li_p_m[i])
else:
  print("NO")

  