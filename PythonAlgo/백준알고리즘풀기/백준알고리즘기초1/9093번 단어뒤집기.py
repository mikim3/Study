# 9093번 단어뒤집기
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    arr = list(map(str,input().rstrip().split(' ')))
    for j in range(len(arr)):
        for z in range(len(arr[j])):
            print(arr[j][-z-1],end = '')
        print(" ",end='')
    print("")