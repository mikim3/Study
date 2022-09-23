
# 직관적으로 큰돈으로 스면 될것 같다.
# 여기서 그리디가 맞는지 확인할려면 정당성을 찾아야한다.

# m , n  = map(int,input().split())
# cnt = 0
# # 큰 단위의 화폐부터 차례대로 확인하기
# coinTypes = []
# for i in range (m):
#     coinTypes.append(int(input()))
# coinTypes.sort(reverse=True)
# for coin in coinTypes:
#     cnt += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
#     n %= coin
# print(cnt)

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

li = []
for i in range(n):
    li.append(int(input()))
total = 0

for i in range(n-1,-1,-1):
    total = total + m // li[i]
    # print("total = ",total,"m = ",m,"li[i]",li[i])
    m = m % li[i]

print(total)

