# 시작시간 1430 마무리시간 1512
import sys
from collections import deque
input = sys.stdin.readline


"""
1   i번쨰 기차에 x번째 좌석에 사람을 태워라
2    i 번째 기차에 x번째 좌석 사람 하차
3  i번째 기차에 승객 전부 한칸씩 뒤로 간다.
    만약 20번째 앉아 있던 사람은 이 명령휴에 하차
4  i 번째 기차에 승객 모두 한칸씩 앞으로 

마지막에 기차의 인원상태를 저장하고
같은 값 있으면 Count X

# 1 0 1 1 

# 0 1 1 0

# 0 0 1 1

# 0 1 1 0

5 5
1 1 1
1 1 2
1 2 2
1 2 3
3 1
"""

n, m = map(int, input().strip().split())
memo = {}
# train = deque(deque(0) * 20 for _ in range(n))
# 리스트안에 deque가  있는 형태
train = []
for i in range(n):
  train.append(deque([0] * 20)) # 이게 됨???
for _ in range(m):
  command = list(map(int,input().strip().split()))
  i = command[1] - 1
  if command[0] == 1:
    x = command[2]
    train[i][x-1] = 1 
  if command[0] == 2:
    x = command[2]
    train[i][x-1] = 0 
  if command[0] == 3:
    train[i].appendleft(0)
    train[i].pop()
  if command[0] == 4:
    train[i].popleft()
    train[i].append(0)
count = 0
# print(train)
for i in range(n):
  now_train = tuple(train[i]) # 
  if now_train not in memo:
    memo[now_train]= 1
    count += 1
    # print("count ==", count,"memo ==", memo)
print(count)