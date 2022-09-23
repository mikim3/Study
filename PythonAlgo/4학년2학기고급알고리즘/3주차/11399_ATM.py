# 시작시간 20:42  20:50
# 기다린 시간의 총합을 최소화 시키는 방법을 찾는 문제

n = int(input())

li_p = list(map(int,input().split()))

li_p.sort()
now_time = 0  # 지금까지 기다려야했던 시간
total = 0  # 사람이 기다린 시간 총합
for i in range(len(li_p)):
    now_time += li_p[i]
    total += now_time

print(total)
