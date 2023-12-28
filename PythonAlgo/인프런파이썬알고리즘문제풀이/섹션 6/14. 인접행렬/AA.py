# 평가 코드는 없긴함
# 무방향 그래프, 방향 그래프 둘다 표현해보기
#

# 무방향 그래프 코드
# 시작시간 231228 21:07 마무리시간 21:20

# 입력값
'''
5 5
1 2
1 3
2 4
3 4
4 5
'''

# 노드갯수, 간선갯수
# n, m = map(int, input().split())
# graph = [[0] * (n + 1) for _ in range(n + 1)]
# #
# for i in range(n):
#   a, b = map(int, input().split())
#   graph[a][b] = 1
#   graph[b][a] = 1

# for i in range(1, n+1):
#   for j in range(1, n+1):
#     print(graph[i][j], end=' ')
#   print()

############################
# 방향, 가중치 그래프
# 입력값
'''
6 9
1 2 7
1 3 4
2 1 2
2 3 5
2 5 5
3 4 5
4 2 2
4 5 5
6 4 5
'''

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

for i in range(1, n + 1):
  for j in range(1, n + 1):
    print(graph[i][j], end=' ')
  print()















