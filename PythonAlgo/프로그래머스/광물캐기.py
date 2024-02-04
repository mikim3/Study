# 시작시간 240204 2153

# 곡괭이 갯수 최대 15개
# 
# 미네랄 50개
# 이정도면 3중 for 문 써도 될듯??

# 피로도가 표만큼 소요됨

# 곡괭이 5개만 캘수 있음
# 곡괭이 한번쓰면 사용할 수 없을때까지 사용
# 광물 순서는 고정임

# 광산에 있는 모든 광물을 캐거나 곡괭이 다쓰면 끝임

# 
# [1,1,1]
# [5,1,1]
# [25,5,1]
from typing import List

def solution(picks, minerals):
  piro = 0
  picks_total_len = sum(picks)
  pick_combination = []
  def dfs(level, tmp_pick_com : List):
    tmp_pick_numof = [0] * (3)
    for i in range(len(tmp_pick_com)):
      if tmp_pick_com[i] == 0:
        tmp_pick_numof[0] += 1
      if tmp_pick_com[i] == 1:
        tmp_pick_numof[1] += 1
      if tmp_pick_com[i] == 2:
        tmp_pick_numof[2] += 1
    # picks에 공괭이 보다 더 많은 곡괭이를 가졌는지 체크
    for i in range(3):
      if tmp_pick_numof[i] > picks[i]:
        return
    # 곡괭이 다 쓴거 or 광물을 다 캔거
    if level == picks_total_len or ((len(minerals) - 1) // 5 + 1) <= level:
      pick_combination.append(tmp_pick_com)
    else:
      for i in range(3):
        dfs(level+1, tmp_pick_com.append(i))
        
        dfs(level+1, tmp_pick_com.append(i))
        
  
  answer = 0
  return answer