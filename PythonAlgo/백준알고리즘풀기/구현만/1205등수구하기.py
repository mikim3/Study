# 21:10시작

# 공동등수는 높은 등수로 모두 표현\
#
import sys

# 주어진 점수갯수, 태수의 점수 , 랭킹리스트에 올릴수 점수의 개수
n, new_score, p = map(int,input().split())
# 현재 랭킹리스트
if (n > 0):
    li = list(map(int,input().split()))
else:
    print(1)
    sys.exit(0)
li.sort(reverse=True)


rank = 0
tmp_score = 0
check = 1
# p 10  n  9
for i in range(p):
    if (i == n):
        rank = i+1
        break
    tmp_score = li[i]
    # 새 점수가 비교점수보다 더 크면
    if (new_score > tmp_score): 
        rank = i+1
        check = 1
        break
    elif (new_score == tmp_score):
        same = 0
        out = False
        # 같은거 개수 계산해서 괜찮으면 rank = i + 1  아니면 check는 0 인 상태로 종료
        for j in range(i, n):
            if (new_score == li[j]):
                same += 1
            if (same + i == p): # 순위권을 벗어남
                out = True
                break
        if (out):
            check = 0
            break
        if (i == p - 1):
            check = 0
            break
        rank = i + 1
        check = 1
        break
    rank = i + 1
if (check == 1):
    print(rank)
else:
    print(-1)
