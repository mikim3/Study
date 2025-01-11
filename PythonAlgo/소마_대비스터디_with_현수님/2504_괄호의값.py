# 시작시간 2330
# 0040에 답봄    

# 숫자 있으면 괄호값 * 숫자값

# 옆에 나열돼 있으면 +
# 안에 들어가 있으면 곱하기계산해야함

# 올바르지 못하면 0 출력

in_value = input()
n = len(in_value)
stack = []
# 0으로 유지돼야 정상
flag = 0
ans = 0
for i in range(n):
  if in_value[i] == '(':
    stack.append('(')
  if in_value[i] == '[':
    stack.append('[')
  if in_value[i] == ')':
    if stack and stack[-1] == '(':
      if in_value[i-1] == '(':
        ans += 2
      else:
        ans *= 2
    else:
      flag = 1
    stack.pop()
  if in_value[i] == ']':
    if stack and stack[-1] == '[':
      if in_value[i-1] == '[':
        ans += 3
      else:
        ans *= 3
    else:
      flag = 1
    stack.pop()
  if flag == 1:
    break
  
if flag == 1:
  print(0)
else:
  print(ans)