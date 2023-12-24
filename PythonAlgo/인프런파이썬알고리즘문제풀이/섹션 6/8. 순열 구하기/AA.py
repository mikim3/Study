##########################
# 시작시간 231224 15:55    마무리시간 1627
# 전에 풀었던 중복순열 구하기를 봐서 풀수 있었음 다시풀기

# 
def DFS(level):
  global count
  if level == m:
    result_sorted = sorted(result)
    # print("result == ",result)
    # print("result_sorted == ",result_sorted)
    for i in range(n):
      if result_sorted[i] != 0:
        if result_sorted[i] == result_sorted[i+1]:
          return
    for i in range(m):
      print(result[i], end=' ')
    print()
    count+=1
  else:
    for i in range(1,n+1):
      result[level] = i
      DFS(level + 1)

count = 0
n, m = map(int, input().split())
result = [0] * (n+1)

DFS(0)
print(count)

#########################
