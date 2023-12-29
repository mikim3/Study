##########################
# 시작시간 231229 2357    마무리시간

# 순열
# 

# 점수 푸는시간 순
# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4

def DFS(level):
  if level == n:
  
  else:
    for i in range(n):
          

n, m = map(int, input().split())
li= []
for i in range(n):
  li.append(list(map(int, input().split())))
print(li)
check= [0] * (n+1)
result = [0] * (n+1)
# 현재 지난 시간
now_time = 0
# 

max_value = 0

#########################
