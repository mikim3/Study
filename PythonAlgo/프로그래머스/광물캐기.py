#################

# 1. 곡괭이를 다 써도 캐지 못할 광물을 걸러낸다.
# 2. 광물을 5개씩 나누어서 2차원 배열로 만든다.
# 3. 


def solution(picks, minerals):
  answer = 0

  # 곡괭이의 수를 구한다.
  sum_picks = sum(picks)
  
  # 곡괭이로 캘 수 있는 광물만큼 자른다.
  num = sum_picks * 5
  if len(minerals) > sum_picks:
    minerals = minerals[:num]
  
  #광물들을 조사한다.
  new_minerals =[[0,0,0] for _ in range((len(minerals) // 5 +1))]
  for i in range(len(minerals)):
    if minerals[i]=='diamond':
      new_minerals[i//5][0]+=1
    elif minerals[i]=='iron':
      new_minerals[i//5][1]+=1
    elif minerals[i]=='stone':
      new_minerals[i//5][2]+=1
  
  print(new_minerals)
  
  #광물의 순서를 다이아몬드, 철, 돌 순서대로 정렬해준다.
  new_minerals.sort(key=lambda x:(-x[0],-x[1],-x[2]))
  print(new_minerals)
  
  #정렬된 광물들을 다이아,철,돌 곡괭이 순서대로 캔다.
  for i in new_minerals:
    dia,iron,stone = i
    for j in range(len(picks)):
      if picks[j]>0 and j==0:
        picks[j]-=1
        answer += dia + iron + stone
        break
      elif picks[j]>0 and j==1:
        picks[j]-=1
        answer += (5*dia) + iron + stone
        break
      elif picks[j]>0 and j==2:
        picks[j]-=1
        answer += (25*dia) + (5*iron) + stone
        break
  return answer
# #######################
# # 시작시간 240204 21:53~ 23:21 +  240205 11:21~12:03 마무리시간 12:03  총 130분 소요
# # 너무 어렵게 풀었음

# from typing import List

# def solution(picks, minerals):
#   picks_total_len = sum(picks)
#   pick_combination = []
#   # 공괭이 조합 사실 최대 15개임
#   tmp_pick_com = [-1] * (20)
#   def dfs(level):
#     tmp_pick_numof = [0] * (3)
#     for i in range(len(tmp_pick_com)):
#       if tmp_pick_com[i] == 0:
#         tmp_pick_numof[0] += 1
#       if tmp_pick_com[i] == 1:
#         tmp_pick_numof[1] += 1
#       if tmp_pick_com[i] == 2:
#         tmp_pick_numof[2] += 1
#     # picks에 공괭이 보다 더 많은 곡괭이를 가졌는지 체크
#     for i in range(3):
#       if tmp_pick_numof[i] > picks[i]:
#         return
#     # 곡괭이 다 쓴거 or 광물을 다 캔거
#     if level == picks_total_len or ((len(minerals) - 1) // 5 + 1) <= level:
#       pick_combination.append(tmp_pick_com.copy())
#     else:
#       for i in range(3):
#         tmp_pick_com[level] = i
#         dfs(level+1)
#         tmp_pick_com[level] = -1
#         # dfs(level+1, tmp_pick_com)
#   dfs(0)
#   # print(pick_combination)
#   piro_min = 999999
#   minerals_len = len(minerals)
#   for i in range(len(pick_combination)):
#     tmp_piro = 0
#     # 캔 미네랄
#     ken_mineral = 0
#     # 곡괭이 1개당 j 
#     for j in range(len(pick_combination[i])):
#       for _ in range(5):
#         if pick_combination[i][j] == 0:
#           tmp_piro += 1
#         elif pick_combination[i][j] == 1 and minerals[ken_mineral] == "diamond":
#           tmp_piro += 5
#         elif pick_combination[i][j] == 2 and minerals[ken_mineral] == "diamond":
#           tmp_piro += 25
#         elif pick_combination[i][j] == 2 and minerals[ken_mineral] == "iron":
#           tmp_piro += 5
#         elif pick_combination[i][j] == 0 or pick_combination[i][j] == 1 or pick_combination[i][j] == 2: 
#           tmp_piro += 1
#         ken_mineral += 1
#         if ken_mineral >= min(minerals_len, picks_total_len*5):
#           break
#       if ken_mineral >= min(minerals_len, picks_total_len*5):
#         break
#     if tmp_piro < piro_min:
#       piro_min = tmp_piro
#   answer = piro_min
#   return answer

# 12
# print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])) # 12
# 50
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])) 
# 반례 테스트 케이스
# 15
print(solution([2, 1, 0], ["diamond","diamond","diamond","diamond","diamond", "iron", "iron","iron","iron","iron", "diamond","diamond","diamond","diamond","diamond"]))
# 19
print(solution([2, 1, 0], ["stone","stone","stone","diamond","diamond", "diamond", "iron","iron","iron","iron", "diamond","diamond","diamond","diamond","diamond"]))
