# 21 33  5 +  22 00    
# 16분걸림
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    li = list(map(str,input().rstrip()))
    li_r =  []
    
    li_r = list(reversed(li))
    
    li = "".join(li)    
    li_r = "".join(li_r)

    li = li.upper()
    li_r = li_r.upper()
    if li == li_r:
        print("#%d YES"%(i+1))
    else:
        print("#%d NO"%(i+1))
    



    
    

