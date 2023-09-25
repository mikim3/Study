##############################
# 시작시간 0925 18:24 마무리시간 18:40

# expression = input() # 입력받은 표현식
# stack = [] # 스택
# res = '' # 출력할 result

# for i in range(len(expression)):
#   if expression[i].isdigit():
#     res += expression[i]
#   elif expression[i] == '(':
#     stack.append(expression[i])
#   elif expression[i] == '*' or expression[i] == '/':
#     while stack and (stack[-1] == '*' or stack[-1] == '/'):
#       res += stack.pop()
#     stack.append(expression[i])
#   elif expression[i] == '+' or expression[i] == '-':
#     while stack and stack[-1] != '(':
#       res += stack.pop()
#     stack.append(expression[i])
#   elif expression[i] == ')':
#     # '()' 사이에 있는 연산은 전부다 pop
#     while stack and stack[-1] != '(':
#       res += stack.pop()
#     stack.pop() # '(' 제거

# while stack:
#   res += stack.pop()
# print(res)

##########################
# 시작시간  0925 17:36   마무리시간 18:13
# 또 답봄
# 2일전에 답을 봤음

# 스택을 쓰자
# 계산순서가 느린거는 뒤로 보낸다. (후위 연산식) 0
# 여기서 규칙들이 나온다.
# 우선순위가 느린 녀석 위주로 append를 하고 그 전에 만난애들이 더 빠른 연산자면 pop()해준다.
# 현재 보고 있는게 이전 것 보다 우선순위가 빠르다면 바로 pop한다.

# (가 나오면 append를 한다.
# )가 나오면 (가 나올때까지 pop한다.


# st = input()
# stack = []
# res = ''
# for x in st:
#   if x.isdigit():
#     res += x 
#   else:
#     if x == '(':
#       stack.append(x)
#     elif x == '*' or x == '/':
#       while stack and (stack[-1] == '*' or stack[-1] == '/'):
#         res += stack.pop()
#       stack.append(x)
#     elif x == '+' or x == '-':
#       while stack and stack[-1] != '(':
#         res += stack.pop()
#       stack.append(x)
#     elif x == ')':
#       while stack and stack[-1] != '(':
#         res += stack.pop()
#       stack.pop()

# while stack:
#   res += stack.pop()
# print(res)
# #########################
