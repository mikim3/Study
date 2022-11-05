
# 0비트 중 가장 오른쪽 비트 1로바꾸기
# 6 -> 7
# 11 -> 15
# 13 -> 15
n = int(input())
# if (n + 1) & ~n == :
su = (n + 1) & ~n
print(n | su)
print(n + su)
