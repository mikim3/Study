# 약 15분걸림

t = int(input())

for i in range(t):
    li = []
    n,s,e,k = map(int, input().split())
    li = list(map(int,input().split()))
    li_cmp = []
    for j in range(s - 1,e):
        li_cmp.append(li[j])
    li_cmp.sort()
    print("#" + str(i+1) + " "+ str(li_cmp[k-1]))
    
### 다시풀기전

# t=int(input())

# for i in range(t):
#     n,s,e,k = map(int,input().split())
#     li = list(map(int,input().split()))
#     li_slice = sorted(li[s-1:e])
#     print("#%d %d"%(i+1,li_slice[k-1]))    
