
# # 답봄

# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# cnt = 0

# # n 개의 단어를 키로가지는 사전 자료형 선언
# S = dict()

# for i in range(n):
#     index = input()
#     # 딕셔너리에 일단 key 값만 넣음
#     S[index] = True    

# for i in range(m):
#     word = input()
#     # n 안에 i 가 있다면 cnt +
#     if word in S:
#         cnt+=1

# print(cnt)
        
# 방법 2 : set()

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
S = set()

for _ in range(n):
    S.add(input())
for i in range(m):
    index=input()
    if index in S:
        cnt+=1
        
print(cnt)
        
        
        
