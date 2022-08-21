
#1463번 문제

# X가 3으로 나누어 떨어지면 3으로 나눈다.
# X가 2로 나누어 떨어지면 2로 나눈다.
# 1을 뺀다.


### 아래처럼 그리디로 풀면 10값은 규칙에 맞지 않아서 제대로 답이 나오지 않는다.
# x = int(input())
# count = 0
# def solution(x,count):
#     if x == 1:
#         print(count)
#         return 
#     if (x % 3 == 0):
#         x = x // 3
#     elif (x % 2 == 0):
#         x = x // 2
#     else:
#         x = x - 1
#     return solution(x, count + 1)

# solution(x, count)

#

f = [0] * (20)
def fibo(n):
    f[0] = 1
    f[1] = 1
    for i in range(2, n + 1,1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
print(fibo(7))


