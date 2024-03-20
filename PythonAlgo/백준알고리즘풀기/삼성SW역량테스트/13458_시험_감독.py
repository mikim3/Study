# 시작시간  0320 15:56 마무리시간 16:16
li = list()
n = int(input())
li = list(map(int,input().split()))
# 한 시험장에 관리 할수 있는 응시자수, 부감독관 감시가능수
b, c = map(int,input().split())

# 감독관의 최숫값을 구하자
count = 0

for i in range(n):
  tmp = li[i]
  tmp -= b
  count += 1
  if tmp > 0:
    count += (tmp - 1) // c + 1
print(count)
