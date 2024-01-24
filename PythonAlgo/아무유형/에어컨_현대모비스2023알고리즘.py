def solution(temperature, t1, t2, a, b, onboard):
  print('temperature ==',temperature,'t1==', t1,'t2==', t2,'a==', a,'b==', b,'onboard==', onboard)
  finish_case = []
  finish_time = len(onboard)
  print('finish_time ==',finish_time)
  def dfs(now_time, now_temperature, cost):
    if now_time == finish_time - 1:
      finish_case.append(cost)
    else:
      for i in range(4):
        # 오른다.
        if i == 0:
          # 값에서 멀어지는쪽으로 이동 X
          if t2 <= now_temperature:
            continue
          # 그렇게 이동했는데 다음에 사람 탔는데 더우면 X
          if onboard[now_time + 1] == 1 and (now_temperature + 1 < t1 or now_temperature + 1 > t2):
            continue
          dfs(now_time+1, now_temperature + 1, cost + a)
        # 내린다.
        elif i == 1:
          # 값에서 멀어지는쪽으로 이동 X
          if t1 >= now_temperature:
            continue
          # 그렇게 이동했는데 실패한 경우의 수 이면 X
          if onboard[now_time + 1] == 1 and (now_temperature - 1 > t2 or now_temperature - 1 < t1):
            continue
          dfs(now_time + 1, now_temperature - 1, cost + a)
        # 유지한다.
        elif i == 2:
          if onboard[now_time + 1] == 1 and (now_temperature > t2 or now_temperature < t1):
            continue
          dfs(now_time + 1, now_temperature, cost + b)
        # 끈다.
        else:
          # 안쪽 온도가 더 따듯함 온도가 내려가겠지
          if now_temperature > temperature:
            if t1 > now_temperature:
              continue
            if onboard[now_time + 1] == 1 and (now_temperature - 1 > t2 or now_temperature - 1 < t1):
              continue
            dfs(now_time + 1, now_temperature - 1, cost)
          elif now_temperature < temperature:
            if t2 < now_temperature:
              continue
            if onboard[now_time + 1] == 1 and (now_temperature + 1 < t1 or now_temperature + 1 > t2):
              continue
            dfs(now_time + 1, now_temperature + 1, cost)
          else:
            if onboard[now_time + 1] == 1 and (now_temperature < t1 or now_temperature > t2):
              continue
            dfs(now_time + 1, now_temperature, cost)
  dfs(0, temperature, 0)
  print(min(finish_case))
  print(finish_case)
  return min(finish_case)

# solution(28,18,26,10,8,	[0, 0, 1, 1, 1, 1, 1]) # 40
solution(-10,-5,5,5,1,[0, 0, 0, 0, 0, 1, 0]) # 25
# solution(11,8,10,10,1,[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]) # 20
# solution(11,8,10,10,100,[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]) # 60
