##########################
# 시작시간  231005    마무리시간
# 답봄
# 전위순회를 생각해야 되는 DFS문제

# node는 현재 방문중인 노드
def dfs(node):
  if node == n + 1:
    for i in range(1, n+1):
      if check[i] == 1:
        print(i, end=' ')
    print()
  else:
    # 아래 두줄이 묶여서 일단 1로 체크하고 다음 노드를 결정하는 기능이 구현됨 
    check[node] = 1
    dfs(node + 1) # 
    # 그후 0을 체크 
    check[node] = 0
    dfs(node + 1)

n = int(input())
check = [0] * (n + 1)
dfs(1) 

