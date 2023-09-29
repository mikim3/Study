###########################
# 인프런 답안
# 리스트에 저장한는 것들에 인덱스도 같이 저장하는 방법을 배움
# any함수도 배움 ( 한가지라도 조건이 성립하면 true반환하는 함수 )

from collections import deque

n, m = map(int, input().split())
que = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
que = deque(que)

count = 0
while True:
  cur = que.popleft()
  if any(cur[1] < x[1] for x in que):
    que.append(cur)
  else:
    count += 1
    if cur[0] == m:
      print(count)
      break


##########################
# 시작시간 230928 21:35    마무리시간 21:55
# 문제자체가 애매하게 적혀졌다고 판단됨

# from collections import deque
 
# n, m = map(int,input().split())
# deq = list(map(int, input().split()))
# deq = deque(deq)

# # m과 인덱스가 일치하는거 옮길때 처리하기
# count = 0
# while deq:
#   if deq[0] == max(deq):
#     if m == 0:
#       print(count + 1)
#       break 
#     deq.popleft()
#     count += 1
#     if m != 0:
#       m -= 1
#     else:
#       m = len(deq) - 1
#   else:
#     tmp = deq.popleft()
#     deq.append(tmp)
#     if m != 0:
#       m -= 1
#     else:
#       m = len(deq) - 1


#########################
