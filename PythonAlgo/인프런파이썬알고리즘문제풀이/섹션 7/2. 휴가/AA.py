##########################
# 시작시간  16:45  마무리시간

# n일 까지만 일 할수 있다.
# 최대 값이 나올수 있는 부분집합
'''
7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
'''
def DFS(level, remain_work):
  # global total
  global max_su
  if level == n:
    now_time = 0
    tmp_su = 0
    for i in range(n):
      if check[i] == 1:
        now_time += li[i][0]
    if now_time <= n:
      for i in range(n):
        if check[i] == 1:
          tmp_su+=li[i][1]
      if tmp_su > max_su:
        max_su = tmp_su
  else:
    check[level] = 1
    if remain_work == 0:
      DFS(level + 1, li[level][0] - 1)
    check[level] = 0
    if remain_work > 0:
      remain_work -= 1
    DFS(level + 1, remain_work)


n = int(input())
li = []
for i in range(n):
  li.append(list(map(int,input().split())))
check = [0] * (n)
max_su = 0
DFS(0, 0)
print(max_su)




#########################
