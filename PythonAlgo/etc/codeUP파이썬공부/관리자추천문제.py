# 3002번문제 기억력테스트3


from bisect import bisect_left,bisect_right  # 이진탐색 라이브러리

def count_by_range(a,left_value,right_value):   #범위안에 값이 몇개 있나 탐색  
    right_index = bisect_right(a,right_value)
    left_index=bisect_left(a,left_value)
    return right_index - left_index
def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index=bisect_left(a,left_value)
    return right_index - left_index


import sys
n=int(input())  # 
a=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(input())  # 질문 m개
b=list(map(int,sys.stdin.readline().rstrip().split()))
equ=0

bisect_left(a,5)  # 



for i in range(m):
    equ=0
    for j in range(n):
        if b[i]==a[j]:
            b[i]=j+1
            equ=1
    if equ==0:
        b[i]=-1

for j in range(m):
    print(b[j],end=' ')

