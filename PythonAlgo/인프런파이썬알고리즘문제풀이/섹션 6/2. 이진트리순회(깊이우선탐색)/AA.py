################
# 시작시간 240318 2249 마무리시간
# if 문을 잘못생각함

def dfs(vector):
  if vector > 7:
    return
  else:
    dfs(2 * vector)
    dfs(2 * vector + 1)
    print(vector, end=' ')

dfs(1)


####################
# # 시작시간 240210  18:27  마무리시간 18:30

# def dfs(vector):
#   if vector > 7:
#     return
#   else:
#     print(vector, end=' ')
#     dfs(vector*2)
#     dfs(vector*2 + 1)
# dfs(1)
# print()

# #####################
# # 231220 복복습
# # 목적
# # 전위순회 후위순회 중위순회 해보기
# def DFS(node):
#   if node > 7:
#     return
#   else:
#     DFS(node * 2)
#     DFS(node * 2 + 1)
#     print(node, end=' ')
# DFS(1)

######################
# 231219 복습
# def DFS(v):
#   if (v > 7): # base condition
#     return
#   else:
#     # 본연의 일을 먼저하고 다음으로 넘어가는 전위순회 방식
#     print(v, end=" ") # 함수 본연의 일을 처리하는 부분(여기서는 그냥 print)
#     DFS(v*2) # 왼쪽 노드
#     DFS(v*2 + 1)# 오른쪽 노드

# # 보통은 전위순회 방식
# # 병합정렬은 후위순회방식ㅋ
# DFS(1)
