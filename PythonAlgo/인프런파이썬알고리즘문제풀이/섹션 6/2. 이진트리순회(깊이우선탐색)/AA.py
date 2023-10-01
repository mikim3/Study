######################
#
def DFS(v):
  if (v > 7): # base condition
    return
  else:
    print(v, end=" ") # 본인 것을 먼저 처리하는 전위 방식
    DFS(v*2) # 왼쪽 노드 
    DFS(v*2 + 1)# 오른쪽 노드

# 보통은 전위순회 방식

# 병합정렬은 후위순회방식

DFS(1)
