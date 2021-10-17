# 3002번문제 기억력테스트

import sys
n=int(input())  # 
a=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(input())  # 질문 m개
b=list(map(int,sys.stdin.readline().rstrip().split()))
equ=0

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

