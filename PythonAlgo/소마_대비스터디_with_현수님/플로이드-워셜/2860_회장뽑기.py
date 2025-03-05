# 시작시간 2229 마무리시간 2241

n = int(input())
li = [[99]* (n+1) for _ in range(n+1)]
while True:
  a,b = map(int,input().split())
  if a==-1 and b==-1:
    break
  li[a][b] = 1
  li[b][a] = 1

for i in range(1,n+1):
  li[i][i] = 0
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      li[i][j] = min(li[i][j], li[i][k] + li[k][j])
# for i in range(len(li)):
#   print(li[i])
li_max = [0] # 0번 사람 0점이 최대
for i in range(1,len(li)):
  tmp = 0
  for j in range(1,len(li[0])):
    if tmp < li[i][j]:
      tmp = li[i][j]
  li_max.append(tmp)
mi = min(li_max[1:])
mi_len = 0
li_hoobo = []
for i in range(len(li_max)):
  if mi == li_max[i]:
    mi_len+=1
    li_hoobo.append(i)
print(f"{mi} {mi_len}")

for i in range(len(li_hoobo)):
  print(li_hoobo[i],end=' ')

