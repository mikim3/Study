##########################
# 시작시간  231217 20:15  마무리시간 20:55?

n = int(input())
li = []
for i in range(n):
  li.append(list(map(int, input().split())))

print(li)
su = 0
for i in range(n):
  if i <= n // 2:
    for j in range(n//2-i, n//2+1+i):
      su += li[i][j]
  else:
    for j in range(i - 2, n - i + 2):
      su += li[i][j]

print(su)

#2
#123
#01234
#123
#2

#n = 5
#








#########################
