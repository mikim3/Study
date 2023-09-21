#############################
# 다시품 시작시간 230921 22:01     마무리시간 23:01
# 이 번에는 밑에 주석을 보고 풀어버림
# 밑에 답안 인듯한 주석이 있어서 참고했는데 그냥 과거에 내가 틀린 소스였음 그래서 시간 더 걸림

# n, m = map(int, input().split())
# n_str = str(n)
# li_n = []

# li_n.append(n_str[0])
# count_pop = 0
# for i in range(1,len(n_str)):
#   if (count_pop != m):
#     for j in range(len(li_n) - 1,-1,-1):
#       if (n_str[i] > li_n[j]):
#         li_n.pop()
#         count_pop += 1
#         if (count_pop == m):
#           break
#   else:
#     for j in range(i,len(n_str)):
#       li_n.append(n_str[j])
#     break
#   # count_pop이 다 쌓이기 전에 append
#   li_n.append(n_str[i])

# if (count_pop != m):
#   for i in range(m - count_pop):
#     li_n.pop()

# for i in range(len(li_n)):
#   print(li_n[i], end='')

#####################
# 선생님 답안

num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for x in num:
  while stack and m > 0 and stack[-1] < x:
    stack.pop()
    m -= 1
  stack.append(x)

if m != 0:
  stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)
