# 시작시간 1650 마무리시간 1711
# 문제 읽는데만 15분씀

n, k = map(int,input().split())
li = list(map(int,input().split()))

li_su = [] # 더한 경우의수
for i in range(n-2):
    for j in range(i+1, n-1):
        for z in range(j+1,n):
            li_su.append(li[i] + li[j] + li[z])
li_su.sort(reverse=True)
count = 1
for i in range(1,len(li_su)):
    if li_su[i] != li_su[i-1]:
        count+=1
    if count == k:
        print(li_su[i])
        break

# # 17분 걸림
# # 
# # for j in range(i + 1,n):  # i + 1이 아니라 그냥 1부터로 실수함   

# # print(li_sum[k - 1]) # k


# n , k = map(int, input().split())

# li = list(map(int,input().split()))
# set_sum = set()

# for i in range(n):
#     for j in range(i + 1,n):
#         for z in range(j + 1,n):
#             set_sum.add(li[i]+li[j]+li[z])
# li_sum = []

# li_sum = sorted(set_sum,reverse=True)

# print(li_sum[k - 1])

# n, k = map(int,input().split())
# li = list(map(int,input().split()))
# li_sum = []
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         for x in range(j+1,len(li)):
#             li_sum.append(li[i] + li[j] + li[x])    
# li_sum_set=list(set(li_sum))
# li_sum_set.sort(reverse=True)
# print(li_sum_set[k-1])
