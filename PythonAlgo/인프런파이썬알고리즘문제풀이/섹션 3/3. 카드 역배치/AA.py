# 11 47
# 문제를 잘못읽음
# 12 15 다시시작
# 7분걸림

# 모범답안
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')
    





# 내가푼 답안
# li = list(range(20))

# for i in range(10):
#     a,b = map(int,input().split())
#     a -= 1 
#     b -= 1
#     a_tmp = a
#     b_tmp = b
#     for i in range((b - a) // 2 + 1):
#         li[a_tmp],li[b_tmp] = li[b_tmp], li[a_tmp]  # 이건 진짜 
#         a_tmp+=1
#         b_tmp-=1
# for i in range(20):
#     li[i] += 1
#     print(li[i],end=' ')
    


    
    
    
    
    
    