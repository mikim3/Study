# 0비트 중 가장 오른쪽 비트 1로바꾸기
# 6 -> 7
# 11 -> 15
# 13 -> 15

n = int(input())

# (n + 1) & ~n을 하면
su = (n + 1) & ~n
print("su==",su)
# print(n | su) 더 하던가 or 연산하면 정답
# print(n + su)
# 위에 꺼가 정답이라고 했는데 사실 아래만 정답임
if (su > n):
    print(n)
else:
    print(n + su)
