# 230618 1728 시작
# 답봄
# 230618 1915 시작         (당일 다시 품)
# 1과 100사이 시간이라는게 힌트가 될수 있는데 잘 이용을 안했다.

a,b,c = map(int, input().split())
time = 100 *[0]
su = 0

for i in range(3):
    start, end = map(int, input().split())
    for j in range(start, end):
        time[j] += 1 #

for i in range(100):
    if time[i] == 1:
        su += a
    elif time[i] == 2:
        su += 2 * b
    elif time[i] == 3:
        su += 3 * c
print(su)
