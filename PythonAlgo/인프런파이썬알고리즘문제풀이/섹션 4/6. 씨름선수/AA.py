# 260213 시작 2030  종료
# 답봄

n = int(input())
li = []
for i in range(n):
  li.append(tuple(map(int,input().split())))
li.sort(key=lambda x : (-x[0],x[1]))
max_w = 0
count = 0
for i in range(n):
  if max_w < li[i][1]:
    count +=1
    max_w = li[i][1]
print(count)

# 시작시간 :  240223 1423   종료시간 :  
# 답봄 근데 솔직히 풀수 있었을듯

# 키순 정렬
# n = int(input())
# li = []
# for i in range(n):
#   li.append(list(map(int,input().split())))

# # 키순 정렬
# li.sort(key = lambda x : (x[0],x[1]), reverse=True)
# # print(li)
# count = 1
# max_weight = li[0][1] 
# for i in range(1, n):
#   if li[i][1] > max_weight:
#     max_weight = li[i][1]
#     count += 1
# print(count)

