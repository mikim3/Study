# 260215 시작 2217 마무리 2251
# 레이저가 발사되는 그림과 끝부분을 보고 직관적으로 조건을 찾아내면 좋은 문제

li = list(input())
stack = []

count = 0
for i in range(len(li)):
    if li[i] == '(':
        stack.append('(')
    if li[i] == ')':
        if li[i-1] == '(': # 레이저 발사
            stack.pop()
            if stack:
                count += len(stack)
        else: # 발사는 아니고
            count += 1
            stack.pop()
print(count)

##########################
# 시작시간    마무리시간
# 답봄 아이디어가 절대 안 떠오름

# 문제 읽는거 부터가 어려움

# bracket = input()
# stack = []

# total = 0
# for i in range(len(bracket)):
#   if bracket[i] == '(':
#     stack.append('(')
#   else:
#     if stack[-1] == '(': # 레이저 쏘는경우
#       stack.pop()
#       total += len(stack)
#     else:
#       stack.pop()
#       total += 1
# print(total)

#########################
