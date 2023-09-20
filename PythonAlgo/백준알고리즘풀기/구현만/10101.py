# 230920 14:35       14:42
# ㅍㅕㄴ하게 풀게해줄 sys.exit() 기억하기?

import sys

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
total = angle1 + angle2 + angle3

if (total != 180):
  print('Error')
  sys.exit()

if (angle1 == 60 and angle2 == 60 and angle3 == 60):
  print('Equilateral')
  sys.exit()
if (angle1 == angle2 or angle1 == angle3 or angle2 == angle3):
  print('Isosceles')
  sys.exit()
else:
  print('Scalene')
