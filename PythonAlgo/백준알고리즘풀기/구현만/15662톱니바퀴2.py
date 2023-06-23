# 230622 17:44시작 ~ 18:40 마무리
# 총4시간정도 고고민민하하고  답  찾아봄
# from collections import deque 기억하기
# deque.rotate(-1) <- 반대로 한칸씩 기억하기

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
# deque가 들어있는 2차원 리스트 선언
wheel = [deque(map(int, input().strip())) for _ in range(T)]

def move(n, d):
  global cur_right, cur_left, wheel
  origne_dir = d

  for i in reversed(range(n)):
    if wheel[i][2] != cur_left:
      cur_left = wheel[i][6]
      wheel[i].rotate(d * -1)
      d*= -1
    else:
      break
  d = origne_dir
  for i in range(n + 1, T):
    if wheel[i][6] != cur_right:
      cur_right = wheel[i][2]
      wheel[i].rotate(d*-1)
      d*= -1
    else:
      break

K = int(input())
for _ in range(K):
  n, d = map(int, input().split())
  cur_left, cur_right = wheel[n-1][6], wheel[n - 1][2]
  wheel[n-1].rotate(d)
  move(n-1, d)
print(sum([1 if wheel[0] else 0 for delta,wheel in enumerate(wheel)]))



# ------------------------------
# 실패한 소스

# import sys
# input = sys.stdin.readline
# # 톱니
# t = int(input())
# li = []
# for i in range(t):
#   li.append(list(input()))
# # 회전횟수
# k = int(input())

# def rotate_t(t_select, dir, li):
#   if (dir == 1):
#     tmp = li[t_select][7]
#     for i in range(7, 0, -1):
#       li[t_select][i] = li[t_select][i - 1]
#     li[t_select][0] = tmp
#   elif (dir == -1):
#     tmp = li[t_select][0]
#     for i in range(7):
#       li[t_select][i] = li[t_select][i+1]
#     li[t_select][7] = tmp
#   print("rotate_t 결과", li)

# for i in range(k):
#   t_select, dir = map(int, input().split())
#   t_select = t_select - 1
#   rotate_t(t_select, dir, li)
#   print("rotate 직후",li)

# su = 0
# for i in range(t):
#   if li[i][0] == '1':
#     su += 1
# print(su)


