# 260216 시작 1644 마무리

li = input()
stack = []

for i in range(len(li)):
  if li[i].isdigit():
    stack.append(li[i])
  elif li[i] == '+':
    t1 = stack.pop()
    t2 = stack.pop()
    stack.append(int(t2) + int(t1))
  elif li[i] == '-':
    t1 = stack.pop()
    t2 = stack.pop()
    stack.append(int(t2) - int(t1))
  elif li[i] == '*':
    t1 = stack.pop()
    t2 = stack.pop()
    stack.append(int(t2) * int(t1))
  elif li[i] == '/':
    t1 = stack.pop()
    t2 = stack.pop()
    stack.append(int(t2) / int(t1))
print(stack[-1])

##########################
# 시작시간 19:21  마무리시간 19:39
# 혼자품

# 앞에서부터 계산
# 연산자를 만나면 계산
# 숫자만 만나면 append()
# 연산자를 만나면 스택맨위에 2개를 pop해서 서로 연산
# 연산결과를 맨위로 올림

# expression = input()
# stack = []
# res = 0

# for x in expression:
#   if x.isdigit():
#     stack.append(int(x))
#   else:
#     # expression에서 더 뒤에 있는 숫자
#     target1 = int(stack.pop()) 
#     target2 = int(stack.pop())
#     if x == '+':
#       stack.append(target2 + target1)
#     elif x == '-':
#       stack.append(target2 - target1)
#     elif x == '*':
#       stack.append(target2 * target1)
#     elif x == '/':
#       stack.append(target2 / target1)


# print(stack.pop())

#########################
