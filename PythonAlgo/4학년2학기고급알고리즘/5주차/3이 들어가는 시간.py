# 시작시간 8시27분  끝낸시간 08시30분
n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for x in range(60):
            if "3" in str(x) + str(j) + str(i):
                count += 1        
print(count)
