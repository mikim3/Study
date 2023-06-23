# 18:48 시작시간
# 애초에 문제를 잘못이해하고 시작함  17분은 그걸로 날림

import sys
input =  sys.stdin.readline

n = int(input())

aTeamScore = 0
bTeamScore = 0
aTeamWinTime = 0
bTeamWinTime = 0
before_time = 0
now_time = 0
last_winner = 0

for i in range(n):
  teamNum, goalTime = map(str,input().strip().split())
  teamNum = int(teamNum)

  minute, second = map(int, goalTime.split(":"))
  min_plus_sec_time = minute * 60 + second
  now_time = min_plus_sec_time
  # 득점한팀 점수 올리기
  if (teamNum == 1):
    aTeamScore += 1
  else:
    bTeamScore += 1

  # 이기고 있던 시간 더해주기
  if (last_winner == 1):
    aTeamWinTime += now_time - before_time
  elif (last_winner == 2):
    bTeamWinTime += now_time - before_time

  # 득점
  if (aTeamScore > bTeamScore):
    last_winner = 1
  elif (bTeamScore > aTeamScore):
    last_winner = 2
  else:
    last_winner = 0
  before_time = min_plus_sec_time

if (last_winner == 1):
  aTeamWinTime += (48 * 60) - now_time
elif (last_winner == 2):
  bTeamWinTime += (48 * 60) - now_time

# 규격에 맞게 바꿈
def makeMMSS(time : str):
  mm,ss = time.split(":")
  if (len(mm) < 2):
    mm = "0" + mm
  if (len(ss) < 2):
    ss = "0" + ss
  return mm + ":" + ss

aTeamWinTimeMMSS = makeMMSS((str(aTeamWinTime // 60) + ":" + str(aTeamWinTime % 60)))
bTeamWinTimeMMSS = makeMMSS((str(bTeamWinTime // 60) + ":" + str(bTeamWinTime % 60)))

print(aTeamWinTimeMMSS)
print(bTeamWinTimeMMSS)
