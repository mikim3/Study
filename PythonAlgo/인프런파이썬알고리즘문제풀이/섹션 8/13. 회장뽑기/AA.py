# 시작시간 2042

n = int(input())
li = [[5000] * (n+1) for _ in range(n+1)]
while True:
  a,b = map(int,input().split())
  if a== -1 and b== -1:
    break
  li[a][b] = 1
  li[b][a] = 1
  
for i in range(1, len(li)):
  li[i][i] = 0
  
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      li[i][j] = min(li[i][j], li[i][k] + li[k][j]) 

# for i in range(len(li)):
#   print(li[i])
li_max = [99999] * (n+1) # 각 사람마다 최댓값

for i in range(1,n+1):
  tmp = 0
  for j in range(1,n+1):
    if li[i][j] > tmp:
      tmp = li[i][j]
  li_max[i] = tmp
# print(li_max)
count = 0
li_hubo = []
for i in range(len(li_max)):
  if min(li_max) == li_max[i]:
    li_hubo.append(i)
    
print(f"{min(li_max)} {len(li_hubo)}")
for i in range(len(li_hubo)):
  print(li_hubo[i], end=' ')