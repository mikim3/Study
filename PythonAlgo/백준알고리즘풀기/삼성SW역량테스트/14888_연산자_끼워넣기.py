# 시작시간 0321 1400 마무리시간 0321 1447 
# 30분만에 풀고 17분동안 문제에 적혀있는 반례찾음 문제를 잘 읽자!!

# 연산자 순서만 바꾸는거

def dfs(level):
  global min_value
  global max_value
  # 연산자 갯수 다 채우면
  if level == n-1:
    tmp = li[0]
    for i in range(n-1):
      if li_operator_list[i] == 0:
        tmp = tmp + li[i + 1]
      elif li_operator_list[i] == 1:
        tmp = tmp - li[i + 1]
      elif li_operator_list[i] == 2:
        tmp = tmp * li[i + 1]
      elif li_operator_list[i] == 3:
        if tmp < 0:
          tmp = (-tmp // li[i + 1]) * -1
        else:
          tmp = tmp // li[i + 1]
    min_value = min(min_value, tmp)
    max_value = max(max_value, tmp)
  else:
    # 4가지 연산자중에 하나를 선택한다.
    # 근데 만약  li_operator에 갯수 조건을 초과하면 그 경우의 수는 보지 않는다.
    # i는 현재 추가하려는 연산자를 의미한다.
    for i in range(4):
      # 조건 초과 안한 경우
      if li_operator_check[i] + 1 <= li_operator[i]:
        li_operator_check[i] = li_operator_check[i] + 1
        li_operator_list.append(i)
        dfs(level+1)
        li_operator_check[i] = li_operator_check[i] - 1
        li_operator_list.pop()

n = int(input())
li = list(map(int, input().split()))
# + - * /
li_operator = list(map(int,input().split()))
# 연산 계산에 넣을때마다 하나씩 값 올려서 몇개 썼는지 체크
li_operator_check = [0] * 4
li_operator_list = []
operator = 0
# for i in range(4):
#   for j in range(li_operator[i]):
#     li_operator2.append(operator)
#   operator += 1
# print(li_operator2)
max_value = -99999999999
min_value = 99999999999

dfs(0)

print(max_value)
print(min_value)

