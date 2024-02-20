# ##########################
# # 시작시간 240220 14:46    마무리시간

# def dfs(now, line):
#   if now[0] == 9:
#     if li[now[0]][now[1]] == 2:
#       print(line)
#       return True
#     else:
#       return False
#   else:
#     for i in range(3):
#       next_x = now[0] + dx[i]
#       next_y = now[1] + dy[i]
#       if 0 <= next_x < 10 and 0 <= next_y < 10 and checked[next_x][next_y] == 0 and (li[next_x][next_y] == 1 or li[next_x][next_y] == 2):
#         checked[next_x][next_y] = 1
#         dfs((next_x, next_y), line)
#         break

# dx = [0,0,1]
# dy = [-1,1,0]

# li = []
# for i in range(10):
#   li.append(list(map(int, input().split())))

# for i in range(10):
#   checked = [[0] * 10 for _ in range(10)]
#   start = (0, i)
#   if li[0][i] == 1:
#     if dfs(start, i):
#       print(i)

# #########################
