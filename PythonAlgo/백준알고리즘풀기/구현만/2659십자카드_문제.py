# 230920 15:12  16:07
# in을 생각 못해서 in만 GPT한테 물어봄

import sys
def make_clock_num(num1, num2, num3, num4):
  li = []
  li.append(num1 +num2 +num3 +num4)
  li.append(num2 +num3 +num4 +num1)
  li.append(num3 +num4 +num1 +num2)
  li.append(num4 +num1 +num2 +num3)
  clock_num = min(li)
  return clock_num

num1, num2, num3, num4 = map(str, input().split())

my_clock_num = make_clock_num(num1, num2, num3, num4)

count = 0
set_all = set()
for i in range(1,10):
  for j in range(1,10):
    for z in range(1,10):
      for x in range(1,10):
        tmp_clock_num = make_clock_num(str(i),str(j),str(z),str(x))
        if tmp_clock_num not in set_all:
          count += 1
          set_all.add(tmp_clock_num)
        if (my_clock_num == str(i)+str(j)+str(z)+str(x)):
          print(count)
          sys.exit()
