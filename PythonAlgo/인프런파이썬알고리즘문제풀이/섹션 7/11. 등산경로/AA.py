##########################
# 시작시간 240114 14:24  마무리시간 15:07

# 다음 경로는 현재 값보다 높아야만 한다.

def dfs(now):
  global count
  # 이렇게 비교 맞나?
  if max_pos == now:
    count += 1
  else:
   for i in range(4):
    next_x = now[0] + dx[i]
    next_y = now[1] + dy[i]
    #
    if 0 <= next_x < n and 0 <= next_y < n and checked[next_x][next_y] == 0 \
      and li[next_x][next_y] > li[now[0]][now[1]]:
      checked[next_x][next_y] = 1
      dfs([next_x, next_y])
      checked[next_x][next_y] = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
li = []
for i in range(n):
  li.append(list(map(int, input().split())))
print(li)
checked = []
for i in range(n):
  checked.append([0] * n)
print('checked== ', checked)
# 가장 낮은 곳 구하기
min_value = 1000000
for i in range(n):
  if min(li[i]) < min_value:
    min_value = min(li[i])
# 가장 높은곳 구하기
max_value = -1
for i in range(n):
  if max(li[i]) > max_value:
    max_value = max(li[i])

for i in range(n):
  for j in range(n):
    if li[i][j] == max_value:
      max_pos = [i,j]
    if li[i][j] == min_value:
      min_pos = [i,j]
checked[min_pos[0]][min_pos[1]] = 1
print('max_pos ==', max_pos, 'min_pos ==', min_pos)
# li[min_pos[0]][min_pos[1]] = 0
count = 0
dfs(min_pos)
print(count)

#########################
