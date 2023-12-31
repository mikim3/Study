##########################
# 시작시간 240101 00:05  마무리시간 00:48

def DFS(level):
  global max_value
  global now_time
  if now_time > m:
    return
  if level == n:
    tmp_result = 0
    for i in range(n):
      if check[i] == 1:
        tmp_result+=li[i][0]
    if max_value < tmp_result:
      max_value = tmp_result
  else:
    check[level] = 1
    now_time+= li[level][1]
    DFS(level+1)
    now_time-= li[level][1]
    check[level] = 0
    DFS(level+1)

n, m = map(int, input().split())
li= []
for i in range(n):
  li.append(list(map(int, input().split())))
# print(li)
# 해당 문제 풀었는지 저장
check= [0] * (n+1)
# result = [0] * (n+1)
# 현재 지난 시간
now_time = 0
max_value = 0
DFS(0)
print(max_value)
#########################
