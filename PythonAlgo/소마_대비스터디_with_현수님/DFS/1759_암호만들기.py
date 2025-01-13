# 시작시간 2156
# DFS로 순열 구하는 문제라는것은 바로 알아챔
# 근데 DFS코드를 까먹어서 유형 익히고 다시 품
# 조합 찾는 문제임


# 최소 한개의 모음
# 최소 두개의 자음
# 오름차순 정렬

# L, C 둘다 3 ~ 15 사이에 굉장히 작은 경우의수를 가지고 있다.
# 15라는 숫자에 15**5 를 해도 겨우 50000정도 나온다. 효율성은 필요 없다.

# start 
def dfs(level, start):
  if level >= l: # 문자열 1세트 완성
    count_mo = 0
    count_ja = 0
    # 결과에서 자음 모음 갯수 세기
    # 결과에서 set로 이미 지나간 문자열인지 조사???? 해야 되나?
    for i in range(l):
      if result[i] == 'a' or result[i] == 'e'or result[i] == 'i'or result[i] == 'o'or result[i] == 'u':
        count_mo += 1        
      else:
        count_ja += 1
    if count_mo >= 1 and count_ja >= 2:
      for i in range(l):
        print(result[i], end = '')
      print()
  else:
    for i in range(start,c):
      # 
      if checked[i] == 0:
        checked[i] = 1 # 사용된 문자 체크
        result[level] = li[i]
        dfs(level + 1, i + 1)
        # dfs재귀 기준 위쪽은 노드에 들어가기전 아래는 노드에서 일한 이후 위로 돌아갈떄
        checked[i] = 0 # 사용된 문자 체크해제

l, c = map(int,input().split())
li = list(input().split())
li.sort()
# visited안에 숫자가 li안에 몇번째 문자를 쓸건지를 의미함
result = [0] * l
# 이미 방문한 문자 체크 (중복 허용X 떼문)
checked = [0] * c
dfs(0, 0)
