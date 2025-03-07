"""
또 풀어라

"""
# n, m = map(int,input().split())
# suik = [[0] * (m+1)]
# for i in range(n):
#   tmp_li = list(map(int,input().split()))
#   suik.append(tmp_li[:])
# # print(f"suik ")
# # for i in range(len(suik)):
# #   print(suik[i])
# # print()
# # dp[tot_money][com_id] = [현재회사'까지' 최대수익금, com_id회사에 투자한 금액]
# # com_id회사에 투자한 금액은 금액 추적용이다. 
# dp = [[[0,0] for _ in range(m+1)] for _ in range(n+1)]

# for com_id in range(1, m+1):
#   for tot_money in range(1, n+1): # 1해도 안해도 같을듯?
#     for now_com_money in range(tot_money+1):
#       max_suik = dp[tot_money][com_id][0] # 현재까지 최대 수익
      
#       now_com_suik = suik[now_com_money][com_id]
#       # 새 수익  com_id-1 해야함 왜냐면 같은 회사 투자 X니까
#       new_suik =dp[tot_money-now_com_money][com_id-1][0] \
#         + now_com_suik  
#       if new_suik > max_suik:
#         dp[tot_money][com_id][0] = new_suik
#         dp[tot_money][com_id][1] = now_com_money
# # print(dp)
# # for i in range(len(dp)):
# #   print(dp[i])
# print(dp[n][m][0])

# # 남은 투자금
# left_tuza = n
# ans = [0] * m
# # 뒤에서 부터 해당 회사에 투자금 만큼만 뺸다.
# for i in range(m, 0, -1):
#   now_tuza = dp[left_tuza][i][1] # 해당 회사에 투자금
#   left_tuza -= now_tuza # 남은 투자금에서 투자한 만큼 뺴기
#   ans[i-1] = now_tuza
# for i in range(len(ans)):
#   print(ans[i],end=' ')


"""
시작시간 1300




"""
# n, m = map(int,input().split())
# # 수익금
# suik = [[0]*(m)]
# for i in range(n):
#   tmp_li = list(map(int,input().split()))
#   suik.append(tmp_li[1:])
# # dp[tot_money][com_id][0] tot_money, com_id 에서 최고의 수익
# # dp[tot_money][com_id][1] com_id 회사에 투자한 비용  
# dp = [[[0,0] for __ in range(m+1)] for _ in range(n+1)]

# # com_id회사까지 투자했을때 dp를 채워나갈거임
# for com_id in range(1, m+1):
#   # com_id 회사들'까지' 투자했을떄 총합돈
#   for tot_money in range(1,n+1):
#     # 그 중 com_id에 투자한 돈
#     for now_com_money in range(tot_money+1):
#       max_suik = dp[tot_money][com_id][0]
#       # 조건 상 현재 회사는 투자 못하니까 이 전까지 중에 골라야함
#       now_com_suik = suik[now_com_money][com_id-1]
#       new_value = dp[tot_money - now_com_money][com_id-1][0] \
#         + now_com_suik

#       if max_suik < new_value:
#         dp[tot_money][com_id][0] = new_value
#         dp[tot_money][com_id][1] = now_com_money
# # for i in range(len(dp)):
# #   print(dp[i])
# print(dp[n][m][0])
# left_tuzagmm = n # 총 투자금
# ans = [0] * m
# for i in range(m,0,-1):
#   now_tuzagmm = dp[left_tuzagmm][i][1]
#   left_tuzagmm -= now_tuzagmm
#   ans[i-1] = now_tuzagmm
# for i in range(len(ans)):
#   print(ans[i], end=' ')


"""
"""
# # 총 투자금액, 기업의 수
# n, m = map(int, input().split())

# suik = [[0]*(m+1)]
# for _ in range(n):
#   a,b,c = map(int,input().split())
#   suik.append([a,b,c])
# # print(suik)
# # dp[total_money][company_id] 
# # n+1은 각각 투자금액이 얼마인 상황을 의미 m+1은 각각의 현재보는 기업을 의미
# # [0,0] -> 현재보는 기업의 -> [최대 수익, 해당 기업에 투자한 금액]
# dp = [[[0,0] for __ in range(m+1)] for _ in range(n+1)]

# # company_id 까지 고려했을때 최적의 total_money 사용한 dp 결과 찾기
# for company_id in range(1, m+1):
#   # 현재 총투자금 total_money dp[company_id][total_money]
#   for total_money in range(1,n+1): 
#     for now_company_money in range(total_money + 1):
#       # 현재까지 최대 수익
#       tuzkgmm = dp[total_money][company_id][0] #     
#       # 지금 회사에 지금 돈 투자했을떄 수익
#       now_company_suik = suik[now_company_money][company_id]
#       # 이전 기업들까지의 수익 + 현재 기업에 투자시 수익
#       # dp[total_money - now_company_money][company_id-1][0]
#       # 그 전에 까지 회사중에서 지금 내가 투자하려는 돈 뻈을때 얻을수 있는 최적의 수익
#       new_value = (dp[total_money - now_company_money][company_id-1][0]\
#           + now_company_suik)

#       if new_value > tuzkgmm:
#         # 새로운 값 넣으면서 현재 회사에 얼마 투자했는지도 넣기
#         dp[total_money][company_id] = [new_value, now_company_money]

# # 최적의 투자 분배 역추적 계산
# total = n
# ans = [0] * m
# for i in range(m, 0,-1):
#   # 마지막에 넣은 회사부터 투자금 분리해서 and넣기
#   tuzkgmm = dp[total][i][1]
#   ans[i-1] = tuzkgmm
#   total -= tuzkgmm

# print(dp[n][m][0])
# for i in range(len(ans)):
#   print(ans[i], end=' ')
  
# 시작시간 2011
"""
꼭 다시 풀기


같은 기업 여러번 투자 안됨 <- 역순으로 채워나가기
dp = [0] * (n+1) # dp[a] = 10 a만원 썼을때 최대 이익 10만원

근데 해당 값을 볼때 해당 회사에 얼마를 넣었을떄 얼마 버는지 다 확인해야함

7 2
1 5 6
2 8 9
3 10 11
4 12 13
5 14 15
6 16 17
7 18 19

2 4
1 1 2 3 4
2 2 3 5 7

"""
# # N: 총 투자 가능한 금액(만원 단위), M: 기업의 수
# N, M = map(int, input().split())

# # 투자 금액별 각 기업의 수익을 저장할 그래프
# # graph[i][j]: i만원을 j번째 기업에 투자했을 때의 수익
# graph = [[0]*(M+1)]  # 0행은 더미 데이터로 초기화
# for _ in range(N):
#   # 각 줄의 첫 숫자는 투자 금액, 나머지는 각 기업의 수익
#   graph.append(list(map(int, input().split())))

# # dp[total_money][company_idx]: total_money만원을 0부터 company_idx번째 기업까지 고려했을 때의
# # 최적 정보. [최대 수익, 해당 기업에 투자한 금액] 형태로 저장
# dp = [[[0,0] for __ in range(M+1)] for _ in range(N+1)]

# # 모든 기업과 투자 금액에 대해 최대 수익 계산
# for company_idx in range(1, M+1):  # 각 기업을 순회
#   for total_money in range(1, N+1):  # 가능한 총 투자 금액을 순회
#     # 현재 기업에 0부터 total_money까지 투자해보는 모든 경우 탐색
#     for now_company_money in range(total_money+1):
#       # 현재까지의 최대 수익
#       value = dp[total_money][company_idx][0]
#       # 이전 기업들까지의 수익 + 현재 기업에 now_company_money 투자시 수익
#       new_value = (dp[total_money-now_company_money][company_idx-1][0] + 
#           graph[now_company_money][company_idx])

#       # 새로 계산한 수익이 기존 수익보다 크면 갱신
#       if new_value > value:
#         dp[total_money][company_idx] = [new_value, now_company_money]

# # 최적의 투자 분배를 역추적하여 계산
# total = N  # 남은 총 투자 금액
# ans = [0]*M  # 각 기업에 투자할 금액을 저장할 배열
# for i in range(M, 0, -1):  # 마지막 기업부터 역순으로
#   value = dp[total][i][1]  # 해당 기업에 투자한 금액
#   ans[i-1] = value  # 결과 배열에 저장
#   total -= value  # 남은 금액 갱신

# # 결과 출력
# print(dp[N][M][0])  # 최대 수익 출력
# print(*ans)  # 각 기업별 투자 금액 출력