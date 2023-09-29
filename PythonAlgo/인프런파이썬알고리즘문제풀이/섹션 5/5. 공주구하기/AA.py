##########################
# 시작시간 230928 11:02   마무리시간 11:54
# 큐를 큐로써 사용하지는 못함
# 큐에는 pop이 없다는 것을 몰랐음

from collections import deque

# def delete_deque_to_index(deq, index):
#   tmp_li = list(deq)
#   tmp_li.pop(index)
#   return deque(tmp_li)

# n, k = map(int, input().split())
# # deq = deque()
# # for i in range(1,n+1):
# #   deq.append(i)

# deq = list(range(1, n+1))
# deq = deque(deq)


# # k랑 shoutNum이 일치할때 제외시킴
# shoutNum = 0
# while n > 1:
#   i = 0
#   while i < len(deq):
#     shoutNum+=1
#     if (shoutNum == k):
#       deq = delete_deque_to_index(deq, i)
#       i -= 1
#       n -= 1
#       shoutNum = 0
#     i += 1
      
# print(deq[-1])

#########################
# 인프런 소스

n , k = map(int, input().split())
dq = list(range(1, n + 1))
dq = deque(dq)

while dq:
  for _ in range(k - 1):
    # 아래 두줄이 원형으로 돌아가는 효과를 준다.
    current = dq.popleft() 
    dq.append(current)
  dq.popleft()
  if len(dq) == 1:
    print(dq[0])
    dq.popleft()
