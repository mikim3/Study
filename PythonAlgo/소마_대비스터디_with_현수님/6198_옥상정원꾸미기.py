# 시작시간 2300 마무리시간
# 답봄
# 나의 관점 자체가 문제를 푸는 방법과 달랐다.
# 나는 각각의 건물하나하나가 본인이 볼수 있는 옥상의 갯수를 세고 
# 각각의 센값을 합치는게 당연하다고 생각하고 풀었지만
# 답이 맞으려면 전체의 갯수를 스택으로 푸는 방법을 생각해야한다.

n = int(input())
li_build = []

for i in range(n):
  li_build.append(int(input()))  

# 스택
stack = []
# 결과값
result = 0

for i in range(n):
  while stack and stack[-1] <= li_build[i]:
    stack.pop()
  stack.append(li_build[i])
  
  result += len(stack) - 1
  
print(result)