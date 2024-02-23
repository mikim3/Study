# 시작시간 :  240223 1456    종료시간 :  15:18
# list   li.pop(0) 이러면 deque queue.popleft()랑 똑같이 작동함


from collections import deque

# 2명까지만 태우기 가능
# Mkg이하로 제한 

n, m = map(int, input().split())
li = list(map(int,input().split()))
li.sort()
print(li)
li.pop(2)
print(li)

queue = deque(li)

# 혼자가야 되는 애들 수
count = 0
while queue:
  if len(queue) >= 2:
    if queue[0] + queue[-1] <= m:
      queue.pop()
      queue.popleft()
      count += 1
    else:
      queue.pop()
      count += 1
  elif len(queue) == 1:
    queue.pop()
    count += 1
  elif len(queue) == 0:
    break
print(count)
