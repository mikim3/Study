##########################
# 시작시간 231226 21:16 마무리시간 22:00
# 못 풀고 강의에서 아이디어만 듣고 풀기시작

def DFS(level, start):
  global count
  if level == m:
    for i in range(m):
      print(result[i], end=' ')
    print()
    count += 1
  else:
    # i가 뜻하는건 현재 level에 넣을 result값임
    for i in range(start - 1, n):
      if check[i] == 0:
        check[i] = 1
        result[level] = i+1
        DFS(level + 1, i + 1)
        check[i] = 0
n, m = map(int, input().split())
check = [0] * n
result = [0] * m
count = 0
DFS(0,1)
print(count)

#########################
