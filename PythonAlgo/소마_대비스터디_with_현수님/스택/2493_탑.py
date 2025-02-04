# 시작시간 1056  마무리시간 1125

# 자기보다 큰게 오른쪽에 있으면 그것보다 왼쪽은 다 필요 없음 스택

# 스택에 있는 값보다 더 크면 스택은 pop 쓸모 없어짐

# append 전에 작은애들 위에서부터 pop 하면됨
# 근데 만약 현재 top이 더 크면 그떄 append

# ㅅ스택에 top보다 작으니 apppend
# append 할떄 top에 있는게 result추가

#

n = int(input())
li = list(map(int,input().split()))
stack = [] # (높이, 인덱스)
stack.append((li[0], 0))
result = [0] * (n)   # 결과   
for i in range(1,n):
  for j in range(len(stack)):
    if stack[-1][0] < li[i]: # li[i] 가 더 크면
      stack.pop() 
    else: # li[i] 가 더 작으면 지금 스택에 top이 부딪히는 거임
      top_height, top_index = stack[-1]
      result[i] = top_index+1
      break
  stack.append((li[i],i))

for i in range(n):
  print(result[i], end=' ')