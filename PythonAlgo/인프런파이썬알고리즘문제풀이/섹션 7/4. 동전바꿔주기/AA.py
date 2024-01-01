##########################
# 시작시간  19:33   마무리시간

# 2중 for 문으로 각 동전별 갯수 표현
def DFS(level):
  global count
  if level == k:
    tmp_sum = 0
    for i in range(k):
      tmp_sum += li[i][0] * check[i]
    if tmp_sum == t:
      count += 1
  else:
    for i in range(k):
      # 각 동전의 갯수만큼 돌기
      for j in range(li[i][1]):
        check[i] += 1
        DFS(level + 1)
        check[i] -= 1

t= int(input())
k = int(input())
li = []
# 몇 번째 동전이 몇개 인지
check = [0] * k
count = 0
for i in range(k):
  li.append(list(map(int,input().split())))
DFS(0)
print(count)

#########################
