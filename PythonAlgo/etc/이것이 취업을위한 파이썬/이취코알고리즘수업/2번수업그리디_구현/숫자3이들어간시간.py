# 숫자3 이 들어간 시간 문제 

# 시간 지나고 다시 풀어봄
# 시작시간 18:15  종료시간 18:25
# 기존에 % 로 했지만 이번에는 str로 바꿔서 파이썬 답게 풀었다.
# 하지만 여전히 문제에 대한 이해력이 딸려서 for i in range(n+1)이 아니라 range(n) 으로해서 시간을 버렸다.

n = int(input())

# 

str_x = ""
str_j = ""
str_i = ""
count = 0
for i in range(n+1):
    for j in range(60):
        for x in range(60):
            if "3" in str(x) + str(j) + str(i):
                count+=1
            # elif "3" in str_j:
            #     count+=1
            # elif "3"  in str_i:
            #     count+=1
print(count)



# n=int(input())

# result=0
# for i in range(0,n+1):  # 시간
#     for j in range(0,60):  # 분
#         for z in range(0,60):  # 초   
#             if i%10==3 or j%10==3 or j//10==3 or z%10==3 or z//10==3:
#                 result+=1         

# print(result)











