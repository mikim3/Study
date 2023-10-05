##########################
# 시작시간 231005 21:50    마무리시간 22:13
# 부분집한 구하기 소스를 보면서 풀음

# 모든 부분집합을 구한다.

# 구하는 과정에서 O는 집합1 X는 집합2에 append한다.

# 각각의 합을 구한다.

import sys

def dfs(node):
  if node == n+1:
    for i in range(1, n+1):
      if check[i] == 1:
        li_1.append(li_input[i-1])
      else:
        li_2.append(li_input[i-1])
    if sum(li_1) == sum(li_2):
      # print("li_1,2",li_1 , "--------", li_2)
      print("YES")
      sys.exit(0)
    li_1.clear()
    li_2.clear()
  else:
    check[node] = 1
    dfs(node + 1)
    check[node] = 0
    dfs(node + 1)

n = int(input())
li_input = list(map(int,input().split()))
li_1 = []
li_2 = []
check = [0] * (n+1)
dfs(1)

print("NO")



#########################
