# 시작시간 2156
# DFS로 순열 구하는 문제라는것은 바로 알아챔
# 근데 DFS코드를 까먹어서 유형 익히고 다시 품

# 최소 한개의 모음
# 최소 두개의 자음
# 오름차순 정렬

# L, C 둘다 3 ~ 15 사이에 굉장히 작은 경우의수를 가지고 있다.
# 15라는 숫자에 15**5 를 해도 겨우 50000정도 나온다. 효율성은 필요 없다.

def dfs(level):
  if level == l: # l개의 문자열 완성
    #
    count_mo = 0
    count_ja = 0
    temp_str = ''
    # 결과로 나온 문자열 출력
    # 결과에서 자음 모음 갯수 세기
    # 결과에서 set로 이미 지나간 문자열인지 조사???? 해야 되나?

    for i in l:
      if
      else:
        count_ja += 1
    if count_ja >= 2 and count_mo >= 1 and not  in res_set:
      print()
  else:
    for i in range(c):

      dfs(level + 1)




l, c = map(int,input().split())
li = list(map(int, input().split()))
li.sort()
res_set = set()


# 알파벳 소문자



