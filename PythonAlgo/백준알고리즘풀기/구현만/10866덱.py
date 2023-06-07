# 시작시간 
# 검색해서 풀음
# deque의 사이즈를 알아낼려면 len(dq) 
# from collections import deque 문법 기억하기

import sys
from collections import deque

input = sys.stdin.readline

dq = deque()
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

n = int(input())
li = []
tmp = ""

for i in range(n):
  cmd = list(input().split())

  if (cmd[0] == 'push_front'):
    dq.appendleft(cmd[1])
  elif (cmd[0] == 'push_back'):
    dq.append(cmd[1])
  elif (cmd[0] == 'pop_front'):
    if (len(dq)):
      print(dq.popleft())
    else:
      print("-1")
  elif (cmd[0] == 'pop_back'):
    if (len(dq)):
      print(dq.pop())
    else:
      print("-1")
  elif (cmd[0] == 'size'):
    print(len(dq))
  elif (cmd[0] == 'empty'):
    if (len(dq) == 0):
      print(1)
    else:
      print(0)
  elif (cmd[0] == 'front'):
    if (len(dq)):
      print(dq[0])
    else:
      print(-1)
  elif (cmd[0] == 'back'):
    if (len(dq)):
      print(dq[-1])
    else:
      print(-1)
