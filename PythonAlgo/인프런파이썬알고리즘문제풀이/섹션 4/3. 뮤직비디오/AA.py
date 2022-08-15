# 시작시간 :  11:35   종료시간 :  

# DVD의 크기를 최소로 하면서  DVD를 m개만 만들어야 한다.
# 
# n 개의 노래길이를 받는다.
# m 개의 DVD만 만든다.
# 

# DVD(한개의)의 최소 길이를 구해라

n, m = map(int, input().split())

li = list(map(int,input().split()))


def Count(capacity):
    cnt = 1
    su = 0
    
    for x in li:
        if su + x > capacity:
            cnt += 1
            su = x
        else:
            su += x
    return cnt

# 전체합과  1 사이에서 선택 알고리즘을 한다.
sum_li = sum(li)
lt = 1
rt = sum_li
res = 0
# mid 보다 같거나 클때까지 li의 값을 더하고 한번짜르고 반복 

while lt <= rt:
    mid = (lt + rt) // 2
    # mid크기로 나눈 갯수구하기
    if Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
    # 너무 작게 나눔
print(res)
