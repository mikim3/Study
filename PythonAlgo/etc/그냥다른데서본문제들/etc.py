
#  프로그래머스
# 로또의 최고 순위와 최저 순위


def solution(lottos, win_nums):
    
    rank=[6,6,5,4,3,2,1]     # 0개맞췄을때 1개 맞혔을때 ......6개모두일치하면 1등

    cnt_0 = lottos.count(0)    # lottos 안의 0의 개수를 반환
    ans = 0       
    for x in win_nums:
        if x in lottos:
            ans += 1
            
    return rank[cnt_0 + ans],rank[ans]
    
print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))


def solution(lottos, win_nums):
    
    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)    # lottos 안의 0의 개수를 반환
    ans = 0       
    for x in win_nums:
        if x in lottos:
            ans += 1
            
    return rank[cnt_0 + ans],rank[ans]



