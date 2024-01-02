##########################
# 시작시간 18:35    마무리시간

# 최대 길이 50
# 반드시 조기종료 조건이 필요하다.

def DFS(level, position):
  global count
  if level == n:
    count +=1
    for i in range(position):
      print(chr(result[i]+64), end=' ')
    print()
  else:
    for i in range(1, 27):
      if code[level] == i:
        result[position] = i
        DFS(level + 1, position + 1)
      elif i >= 10 and code[level] == i//10 and code[level+1] == i % 10:
        result[position] = i
        DFS(level + 2, position + 1)

# 1을 우선으로
# 2를 후 순위로 바꿔주기
code = list(map(int, input()))
n = len(code)
#
code.insert(n, -1)
result = [0] * (n+3)
count = 0
DFS(0, 0)
print(count)

#########################
