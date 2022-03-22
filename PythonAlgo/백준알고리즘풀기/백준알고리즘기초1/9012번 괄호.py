# 9012번 괄호
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    arr = input().rstrip()
    sum = 0 
    for j in range(len(arr)):
        if arr[j] == '(':
            sum += 1
        elif arr[j] == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")

