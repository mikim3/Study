# 시작시간 23:05 

# # 소괄호 스택
# li_little = []
# # 대괄호 스택
# li_big = []
# # 그냥 문장
# li = []
# # yes no
# select = ""

# while True:
#     li = input()
#     if li[0] == ".":
#         break
#     else:
#         for i in range(len(li)):
#             if li[i] == "(":
#                 li_little.append(li[i])
#             elif li[i] == ")":
#                 # li_little이 비어있으면
#                 if not li_little:
#                     select = "no"
#                     break
#                 li_little.pop()
#             elif li[i] == "[":
#                 li_big.append(li[i])
#             elif li[i] == "]":
#                 if not li_big:
#                     select = "no"
#                     break
#                 li_big.pop()
#         if select == "no":
#             print("no")
#         else:
#             print("yes")
#         li_big.clear()
#         li_little.clear()
#         select = ""
                
# print("finish")

while True:
    s = input()
    if s == '.':
        break
    stk = []
    temp = True
    for i in s:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if not stk or stk[-1] == '[':
                temp = False
                break
            elif stk[-1] == '(':
                stk.pop()
        elif i == ']':
            if not stk or stk[-1] == '(':
                temp = False
                break
            elif stk[-1] == '[':
                stk.pop()
    if temp == True and not stk:
        print('yes')
    else:
        print('no')
