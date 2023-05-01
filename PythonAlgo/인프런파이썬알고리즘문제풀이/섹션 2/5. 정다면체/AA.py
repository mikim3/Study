# 1652  시작  1710 마무리

# 리스트 0으로 초기화 하는법 서칭함
# li = [0 for i in range(n + m + 1)]
n, m = map(int, input().split())

li = [0 for i in range(n + m + 1)]

for i in range(1,n + 1):
    for j in range(1,m + 1):
        li[i + j] += 1 
max_value = max(li)

for i in range(len(li)):
    if (li[i] == max_value):
        print(i, end=' ')


# collections.defaultdict(int)는 서칭해서 기억해냄 
# 35분걸림

# 딕셔너리로 내가 품

# import collections
# n,m = map(int,input().split())
# dic = collections.defaultdict(int)

# for i in range(1,n+1):
#     for j in range(1,m+1):
#         dic[i+j] += 1 
# li_max = [k for k,v in dic.items() if max(dic.values()) == v]  # 리스트 컴프리헨션으로 딕셔너리 최대값 출력

# for i in li_max:
#     print(i,end=' ')

# 리스트로 해보기

# n,m = map(int,input().split())
# li = [0]* (n+m+3)

# for i in range(1,n+1):
#     for j in range(1,m+1):
#         li[i+j] += 1 
# max = 0

# for i in range(len(li)):
#     if li[i] > max:
#         max = li[i] 
# for i in range(len(li)):
#     if li[i] == max:
#         print(i,end=' ')



