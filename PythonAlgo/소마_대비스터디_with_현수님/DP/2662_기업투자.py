# 시작시간 2011
"""
꼭 다시 풀기


# 같은 기업 여러번 투자 안됨 <- 역순으로 채워나가기
dp = [0] * (n+1) # dp[a] = 10 a만원 썼을때 최대 이익 10만원

근데 해당 값을 볼때 해당 회사에 얼마를 넣었을떄 얼마 버는지 다 확인해야함

"""
# N: 총 투자 가능한 금액(만원 단위), M: 기업의 수
N, M = map(int, input().split())

# 투자 금액별 각 기업의 수익을 저장할 그래프
# graph[i][j]: i만원을 j번째 기업에 투자했을 때의 수익
tuza = [[0]*(M+1)]  # 0행은 더미 데이터로 초기화
for _ in range(N):
  # 각 줄의 첫 숫자는 투자 금액, 나머지는 각 기업의 수익
  tuza.append(list(map(int, input().split())))

# dp[total_money][company_idx]: total_money 만원을 0부터 company_idx번째 기업까지 고려했을 때의
# 최적 정보. [최대 수익, 해당 기업(현재company_idx)에 투자한 금액] 형태로 저장
dp = [[[0,0] for __ in range(M+1)] for _ in range(N+1)]

# 모든 기업과 투자 금액에 대해 최대 수익 계산
for company_idx in range(1, M+1):  # 각 기업을 순회
  for total_money in range(1, N+1):  # 가능한 총 투자 금액을 순회
    # 현재 기업에 0부터 total_money까지 투자해보는 모든 경우 탐색
    for now_company_money in range(total_money+1):
      # 현재까지의 최대 수익
      value = dp[total_money][company_idx][0]
      # 이전 기업들까지의 수익 + 현재 기업에 now_company_money 투자시 수익
      new_value = (dp[total_money-now_company_money][company_idx-1][0] + 
          tuza[now_company_money][company_idx])

      # 새로 계산한 수익이 기존 수익보다 크면 갱신
      if new_value > value:
          dp[total_money][company_idx] = [new_value, now_company_money]

# 최적의 투자 분배를 역추적하여 계산
total = N  # 남은 총 투자 금액
ans = [0]*M  # 각 기업에 투자할 금액을 저장할 배열
for i in range(M, 0, -1):  # 마지막 기업부터 역순으로
  value = dp[total][i][1]  # 해당 기업에 투자한 금액
  ans[i-1] = value  # 결과 배열에 저장
  total -= value  # 남은 금액 갱신

for i in range(len(dp)):
  print(dp[i])

# 결과 출력
print(dp[N][M][0])  # 최대 수익 출력
print(*ans)  # 각 기업별 투자 금액 출력