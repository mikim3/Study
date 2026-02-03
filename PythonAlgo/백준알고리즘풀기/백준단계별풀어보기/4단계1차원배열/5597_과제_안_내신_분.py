# 시작시간 2058 마무리시간
# 답봄

# 배열로 풀기
# submitted = [False] * 31 #

# for _ in range(28):
#     x = int(input())
#     submitted[x] = True

# for i in range(1,31):
#     if not submitted[i]:
#         print(i)

# #----------------
# # 차집합으로 풀기

# all_students = set(range(1,31))
# submitted = set()

# for _ in range(28):
#     submitted.add(int(input()))

# missing = sorted(all_students - submitted)
# print(missing[0])
# print(missing[1])

