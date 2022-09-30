#

# 일단 문제의 이해가 어려웠다.


# 17 8
# 2
# 2 16

# 주어진 A진법 표현할 B진법
# A는 2개의 수로 이루어져있다.
# 두번째 자리수는 2 첫번째 자리수는 16이다.

#6 2

A_zin, B_zin = map(int, input())
m = int(input())
A = list(map(int, input().split()))

# A를 10진법으로 변환
A_10 = 0
for i in range(len(A)):
    A_10 += A[i]*(A_zin ** (i + 1)) 

# A의 10진법 값을 B진법으로 변환

while ()


         






