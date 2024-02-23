# 시작시간 :  240223 14:41   종료시간 : 1455 

l = int(input())
li = list(map(int,input().split()))
m = int(input())

for i in range(m):
  li.sort()
  li[0] = li[0] + 1
  li[-1] = li[-1] - 1
li.sort()
print(li[-1] - li[0])
    
