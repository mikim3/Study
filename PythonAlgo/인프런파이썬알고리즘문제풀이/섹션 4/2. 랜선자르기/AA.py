# 시작시간 :  11 25   종료시간 :  

k , n = map(int, input().split())

li = []
for i in range(k):
    li.append(int(input()))

max_value = max(li)
max_index = li.index(max_value)

lt = 0
rt = max_value 
div = 0
mid = (lt + rt) // 2

while lt <= rt:
    for i in range(len(li)):
        div += li[i]//mid
    if div <= n:
        rt = mid - 1
    elif div > n:
        lt = mid + 1
        res = div
        
    
print(res)    
    
    