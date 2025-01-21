# 시작시간 1929 마무리시간
# 공청기는 -1
#

# 공청기로 들어간 공기는 정화된다.

# 5
# 5 - [5/5] * 2방향 == 3
import copy
import sys
input = sys.stdin.readline

# 확산 처리를 하는 함수
def hawk_san(li_change):
  for i in range(r):
    for j in range(c):
      if li[i][j] == -1 or li[i][j] == 0:
        continue
      elif li[i][j] > 4: # 0보다 크다고 해도 똑같음
        change = li[i][j] // 5
        can_hawk_san = 0 # 확산 가능한 곳
        for z in range(4): # 확산 가능한지 판별
          next_x = i + dx[z]
          next_y = j + dy[z]
          if next_x < 0 or next_x >= r or next_y < 0 or next_y >= c:
            continue
          if li[next_x][next_y] == -1: # 공청기에 막힘
            continue
          else:
            can_hawk_san += 1 # 확산 가능한 공간임
            li_change[next_x][next_y] += change
        li_change[i][j] -= change * can_hawk_san # 확산된 공간 만큼 빼주기
  for i in range(r):
    for j in range(c):
      li[i][j] += li_change[i][j]

def air_purifier(air_top, air_bottom, li):
  li_tmp = copy.deepcopy(li)  # li 복사 마지막에 li_tmp에 값을 li로 옮기기

  for j in range(1, c - 1): # 오른쪽으로 바람부는애들
    li_tmp[air_top][j + 1] = li[air_top][j] #
  for i in range(air_top,0,-1): # 위로 바람
    li_tmp[i - 1][c - 1]  = li[i][c - 1]
  for j in range(c - 1, 0, -1): # 왼쪽으로 바람부는애들
    li_tmp[0][j - 1] = li[0][j]
  for i in range(0, air_top - 1): # 아래로 바람
    li_tmp[i + 1][0]  = li[i][0]
  for j in range(1, c - 1): # 오른쪽으로 바람부는애들
    li_tmp[air_bottom][j + 1] = li[air_bottom][j]
  for i in range(air_bottom, r - 1): # 아래로 바람
    li_tmp[i + 1][c-1]  = li[i][c-1]
  for j in range(c - 1, 0, -1): # 왼쪽으로 바람부는애들
    li_tmp[r-1][j - 1] = li[r-1][j]
  for i in range(r-1, air_bottom + 1, -1): # 위로 바람
    li_tmp[i - 1][0]  = li[i][0]
  li_tmp[air_top][1]= 0
  li_tmp[air_bottom][1]= 0
  for i in range(r):
    for j in range(c):
      li[i][j] = li_tmp[i][j]



  # if li[air_top][] : # 오른쪽으로 바람분다.

dx = [-1,0,1,0]
dy = [0,1,0,-1]
li = []
# row, col에서 time이 지난후 결과
r, c, t = map(int,input().strip().split())

for i in range(r):
  li.append(list(map(int,input().strip().split())))

# t시간동안 동작
for i in range(t):
  li_change = [[0] * c for _ in range(r)] # 변화값을 기록한 리스트
  hawk_san(li_change)
  for i in range(r):
    if li[i][0] == -1:
      air_purifier(i, i+1, li)
      break
  # print("#######공청기이후######")
  # for i in range(r):
  #   print(li[i])
total = 0
for i in range(r):
  for j in range(c):
    total += li[i][j]
total += 2 # 공청기 값

print(total)

