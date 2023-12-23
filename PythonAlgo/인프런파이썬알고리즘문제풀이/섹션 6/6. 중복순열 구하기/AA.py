##########################
# 시작시간  231223 1727  마무리시간 1824
# '==' 을 써야 될 곳에 '>'을 써서 30분 날림 원래는 1754에 풀음

def DFS(level):
  if level == m:
    for i in range(m):
      print(result[i], end=' ')
    print()
  else:
    for i in range(n):
      result[level]= i+1
      DFS(level + 1)

n, m = map(int, input().split())
result = [0] * (n + 1)
DFS(0)

#########################
