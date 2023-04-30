# 17분 걸림
# 
# for j in range(i + 1,n):  # i + 1이 아니라 그냥 1부터로 실수함   

# print(li_sum[k - 1]) # k


n , k = map(int, input().split())

li = list(map(int,input().split()))
set_sum = set()

for i in range(n):
    for j in range(i + 1,n):
        for z in range(j + 1,n):
            set_sum.add(li[i]+li[j]+li[z])
li_sum = []

li_sum = sorted(set_sum,reverse=True)

print(li_sum[k - 1])

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
