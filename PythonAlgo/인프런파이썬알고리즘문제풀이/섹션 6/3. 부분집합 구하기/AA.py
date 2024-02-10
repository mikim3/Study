############################
# 시작시간 240210 18:31 마무리시간 18:41

def dfs(level):
  if level >= n:
    # print(checked)
    for i in range(n):
      if checked[i] == 1:
        print(i+1, end=' ')
    print()
  else:
    checked[level] = 1
    dfs(level+1)
    checked[level] = 0
    dfs(level+1)

n = int(input())
checked = [0] * (n + 1)
dfs(0)
# print()

#############################

# def DFS(node):
#   if node > n:
#     for i in range(1, n + 1):
#       if check[i] == 1:
#         print(i, end=' ')
#     print()
#   else:
#     check[node] = 1
#     DFS(node + 1)
#     check[node] = 0
#     DFS(node + 1)
  
# n = int(input())
# check = [0] * (n+1)
# DFS(1)

##############################
# 시작시간 231221 0000 마무리시간 0010
# DFS로 선택한다 만다를 결정할 수 있음
# 결국 답을 봤음  check = [0] * (n+1) 부분 봄

# def DFS(node):
#   if node > n:
#     for i in range(1,n+1):
#       if check[i] == 1:
#         print(i, end=' ')
#     print()
#   else:
#     check[node] = 1
#     DFS(node + 1)
#     check[node] = 0
#     DFS(node + 1) 
# n = int(input())
# check = [0] * (n+1)
# DFS(1)


#############################
# 시작시간 231219 20:30 마무리시간
# 영상 바로봄

# def DFS(node):
#   # 만약에 원하는 레벨보다 높으면 그 집합을 출력
#   if node == n+1:
#     for i in range(1,n+1):
#       if check[i] == 1:
#         print(i, end=' ')
#     print()
#   else:
#     # 1,0 으로 해당 값을 집합에 넣을지 말지 결정
#     check[node] = 1
#     DFS(node+1)
#     check[node] = 0
#     DFS(node+1)
# n = int(input())
# check = [0] * (n+1)
# DFS(1)

#############################
# 시작시간 231006 16:01 # 마무리시간 16:12

# def dfs(node):
#   if node == n + 1:
#     for i in range(1, n+1):
#       if check[i] == 1:
#         print(i, end=' ')
#     print()
#   else:
#     check[node] = 1
#     dfs(node + 1)
#     check[node] = 0
#     dfs(node + 1)

# n = int(input())
# check = [0] * (n+1)
# dfs(1)

##########################
# 시작시간  231005    마무리시간
# 답봄
# 전위순회를 생각해야 되는 DFS문제

# # node는 현재 방문중인 노드
# def dfs(node):
#   if node == n + 1:
#     for i in range(1, n+1):
#       if check[i] == 1:
#         print(i, end=' ')
#     print()
#   else:
#     # 아래 두줄이 묶여서 일단 1로 체크하고 다음 노드를 결정하는 기능이 구현됨
#     check[node] = 1
#     dfs(node + 1) #
#     # 그후 0을 체크
#     check[node] = 0
#     dfs(node + 1)

# n = int(input())
# check = [0] * (n + 1)
# dfs(1)

