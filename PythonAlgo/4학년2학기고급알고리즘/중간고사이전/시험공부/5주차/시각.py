# 시작시간 11:00 끝낸시간 11:04


n = int(input())

result = 0
for i in range(n+1):
    for j in range(60):
        for x in range(60):
            time_result = str(i) + str(j) + str(x)
            if '3' in time_result:
                result += 1

print(result)