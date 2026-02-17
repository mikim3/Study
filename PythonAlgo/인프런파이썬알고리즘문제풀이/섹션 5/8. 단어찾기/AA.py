# 260216 시작 2149 마무리 2210
from collections import deque
n = int(input())
dq = deque()
li = []
for i in range(n):
  dq.append(input())
for i in range(n-1):
  se = input()
  while True:
    tmp = dq.popleft()
    if tmp != se:
      dq.append(tmp)
    else:
      break
print(dq[0])

##########################
# 시작시간 21:27    마무리시간 21:33

# n = int(input())
# li = []

# for i in range(n):
#   li.append(input())

# for i in range(n-1):
#   input_word = input()
#   if input_word in li:
#     li.remove(input_word)

# print(li[0])

#########################
