# 시작시간 1756 마무리시간


# Ai 보다 오른쪽에 있는 배열을
# 슬라이싱해서
# 슬라이싱 된 애들중에 가장 왼쪽에 있는데
# Ai보다는 큰애를 찾는데
# 시간복잡도가 빡세다.

# 이미 문제에서 주려는 수열의 크기가 10**6임   (nlogn 은 가능)
# 그럼 값 하나당  
#  10**8
# Ai [:]   

n = int(input())
li = list(map(int,input().split()))

# 4
# 9 5 4 8 

# s: 9 8 7 
# s(X): 9 5 8

# map <- 모든언어 공용용어 자료구조 용어
dic = {"key" : "value"}  # 퍼아쏜 전용


# [(value, index)] 
stack = [(li[0],0)]
li_result = [0] * (n)  # 마지막에 출력할 리스트
i = 1
while i < n:
  if stack:
    top_value, top_index = stack[-1]  
    if top_value < li[i]: # 스택 맨위에 값이 현재보려는 값보다 작은경우 이 경우 스택맨위값이 더 큰게 만날떄까지 계속 pop
      while stack and top_value < li[i]:
        top_value, top_index = stack.pop()
        li_result[top_index] = li[i]
        if stack:
          top_value, top_index = stack[-1]
      stack.append((li[i], i))
      i += 1
    elif top_value >= li[i]: # 새로온 값이 현재 탑보다 작음
      stack.append((li[i], i))
      i += 1
  else:
    stack.append((li[i], i)) 
    i += 1
for i in range(n):
  if li_result[i] == 0:
    li_result[i] = -1

# li_result.append(-1) # 맨끝은 무조건 -1
for i in range(n):
  print(li_result[i], end=' ')
