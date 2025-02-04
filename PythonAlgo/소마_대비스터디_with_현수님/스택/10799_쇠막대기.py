# 시작시간 1000 마무리시간
import sys
input = sys.stdin.readline

li= list(input().strip())
li.append(-1) # 끝 공간 추가
stack = []
n = len(li)
count = 0
i = 0
while i < n:
  # print('i ==',i)
  if li[i] == '(' and li[i+1] == ')': # 레이저 비임
    # print("비임")
    i += 1
    if stack:
      for j in range(len(stack)):
        stack[j] += 1
  elif li[i] == '(': # 막대 시작
    stack.append(1)
  elif li[i] == ')':  # 막대끝임
    mak_dae = stack.pop()
    # print("값 더함", mak_dae)
    count += mak_dae
  print(stack, "   ", count)
  i += 1
  if li[i] == -1:
    break
print(count)  

# 빔쏘면 스택만큼 +
# 그냥 닫히면 스택만큼 +  하면서 pop

# 3 2 5 5 2

# 