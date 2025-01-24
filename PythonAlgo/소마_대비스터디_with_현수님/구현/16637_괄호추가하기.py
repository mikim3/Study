# 시작시간 1017 마무리시간

# 입력 숫자는 한자리수
# 괄호를 내 맘대로 추가 해서 가장 큰수 만들기
# N(1 ≤ N ≤ 19)
# 

def dfs(level):
  if level >= m:

    # checked 한세트 완성
    
    # max값 구해라
    
  else:
    # 앞이랑 뒤가 1이면() 본인은 1이될수 없음
    if 앞에가 O면 난 X:
      checked[level] = 1
    dfs(level+1)
    checked[level] = 0
    dfs(level+1)

n = int(input())
li = list(map(int, input().split()))
m = len(li) // 2 # 연산자 갯수
max = 0 # 최댓값 저장
checked = [0] * (m+1)
# 

dfs(0)
