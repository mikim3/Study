# 시작시간 1657 마무리시간
# 답봄  #다시 풀자

# 인덱스, 벨류로 저장
# sort로 벨류기준 정렬
# set에 저장
# 다시 리스트로 변환해서 중복제거

# 딕셔너러에 저장

n = int(input())
li = list(map(int,input().split()))
li_not_dupli = sorted(list(set(li))) # 대소비교용 중복제거
# print(li_not_dupli)
memo = {li_not_dupli[i]: i for i in range(len(li_not_dupli))}
for i in li:
  print(memo[i],end=' ')
