# 260212 시작 2149 마무리 
# 답봄

n = int(input())
li = []
for i in range(n):
    start, end = map(int,input().split())
    li.append((start,end))
li.sort(key = lambda x : (x[1],x[0]))
now_t = 0
count = 0
for start,end in li:
    if start >= now_t:
        count += 1
        now_t = end
print(count)
################
# 시작시간 240223 1045 마무리시간
# 답봄
# 5
# 1 4
# 2 3
# 3 5
# 4 6
# 5 7

# n = int(input())
# li = []
# for i in range(n):
#   li.append(list(map(int,input().split())))
# li.sort(key= lambda x : (x[1], x[0]))
# #
# # print(li)

# pre_end = 0
# count = 0
# for start, end in li:
#   if start >= pre_end:
#     count += 1
#     pre_end = end
# print(count)


# 시작시간 :     종료시간 :  

# n = int(input())
# meeting=[]
# for i in range(n):
#     a, b=map(int, input().split())
#     meeting.append((a, b))
# meeting.sort(key=lambda x : (x[1], x[0]))
# et=0
# cnt=0
# for x, y in meeting:
#     if x>=et:
#         et=y
#         cnt+=1
# print(cnt)