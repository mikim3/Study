# 22 38  23 16 분까지 풀어도 시간초과나옴

# 답지

n , m = map(int,input().split())
li = list(map(int,input().split()))
lt = 0
rt = 1
tot = li[0]
cnt = 0
while True:
    if tot < m:
        if rt<n:
            tot += li[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= li[lt]
        lt += 1
    else:
        tot -= li[lt]
        lt += 1

print(cnt)
    
#### 내가푼 답안

# n , m = map(int,input().split())

# li = list(map(int,input().split()))
# tot = 0
# lt = 0 
# rt = 0
# cnt = 0
# for lt in range(n):
#     for rt in range(lt + 1, n):
#         # print(rt)
#         tot = sum(li[lt:rt+1])
#         if tot < m:
#             pass
#         elif tot == m:
#             cnt += 1
#             # print("lt, rt",lt, rt)
#             # print("tot",tot)
#             # print("cnt", cnt)
#             break
#         else:
#             break
# print(cnt)