# 사용시간 1431 1458
# 답봄
# 문제의 말뜻을 이해를 못했다. 말뜻만 이해하면 쉬운 문제였다.

from collections import deque
n, k = map(int, input().split())
queue = deque([])

for i in range(1,n+1):
    queue.append(i)

print("<",end="")
while len(queue)>=2:
    for i in range(k-1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(),end=", ")
print(queue.popleft(),end="")
print(">",end="")
