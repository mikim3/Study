
t=int(input())

for i in range(t):
    n,s,e,k = map(int,input().split())
    li = list(map(int,input().split()))
    li_slice = sorted(li[s-1:e])
    print("#%d %d"%(i+1,li_slice[k-1]))    
