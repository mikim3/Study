# 다시풀어보기














# # 시작시간 2150 마무리시간

# # 답봄
# # 중복참조 문제로 못 품

n, m = map(int, input().split())
li = []
for now_q in range(n):
    li.append(list(map(int, input().split())))
dp = [-9999] * (m+1) 
dp[0] = 0

for now_q in range(n):
    t,v = li[now_q][1], li[now_q][0]
    # 뒤에서부터 갱신
    for now_time in range(m, t-1, -1):  # t 이상인 시간만 고려
      if dp[now_time] < dp[now_time - t] + v:
        dp[now_time] = dp[now_time-t] + v

print(max(dp))
# print(dp2)