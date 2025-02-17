# 답봄
import sys
input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
universe = defaultdict(int)

for _ in range(m):
    # 행성 입력 받기
    planets = list(map(int, input().split()))
    # print("planets ===", planets)
    # 행성 정렬 ( 구성 같은 행성 한개만 세기 )
    sortedPlanets = sorted(list(set(planets)))
    
    # 행성 순위 지정
    rank = {sortedPlanets[i] : i for i in range(len(sortedPlanets))}
    print("rank ===", rank)
    # 입력 받은 행성에 맞게 순위 저장
    vector = tuple([rank[i] for i in planets])
    
    # 해당 순위 벡터에 대한 개수 추가
    universe[vector] += 1
    
    print("universe",universe)
    
sum = 0

for i in universe.values():
    # n개 중 2개의 우주를 엮어야 하기 때문에 n C 2 를 해줘야 함 (중복 제외)
    sum += (i * (i - 1)) // 2 # nC2
    
print(sum)



# # 시작시간 1546 마무리시간
# import copy
# import sys
# sys.setrecursionlimit(10000000)
# input = sys.stdin.readline
# """

# # 각각에 대하여 균등한지 모두 구해야함
# # 일단 "각각" -> m개 중에 2개를 뽑는 모든 조합을 나타냄

# # 각각 에 대해 균등한지 균등하지 않은지 여부를 파악하면됨

# 2 3
# 1 3 2
# 12 50 31

# """
# def fair_space(a,b): #
#   fair = 1 # 1이면 균등
#   a_li = copy.deepcopy(li[a]) # 아마도 n시간 복잡도
#   b_li = copy.deepcopy(li[b])
  
  
  
#   return fair

# def dfs(level,start): # m개중에 2개를 뽑는 조합의 시간 복잡도
#   global count
#   if level >= 2:
#     count += fair_space(combi[0], combi[1]) # 
#   else:
#     for i in range(start, m):
#       combi[level] = i
#       dfs(level+1, i+1)
#       combi[level] = 0 # 없어도 될듯

# m, n = map(int, input().strip().split())
# li = []
# for i in range(m):
#   li.append(list(map(int,input().strip().split())))
# count = 0
# combi = [0] * (2)
# dfs(0,0)
# print(count)

