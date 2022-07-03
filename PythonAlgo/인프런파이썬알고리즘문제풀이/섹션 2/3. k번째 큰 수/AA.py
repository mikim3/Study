
n, k = map(int,input().split())
li = list(map(int,input().split()))
li_sum = []
for i in range(len(li)):
    for j in range(i+1,len(li)):
        for x in range(j+1,len(li)):
            li_sum.append(li[i] + li[j] + li[x])    
li_sum_set=list(set(li_sum))
li_sum_set.sort(reverse=True)
print(li_sum_set[k-1])
