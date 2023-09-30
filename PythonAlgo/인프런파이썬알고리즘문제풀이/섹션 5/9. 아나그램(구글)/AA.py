############################
# 230930 인프런 개선된 답안

a = input()
b = input()
sH = dict()

for x in a:
  sH[x] = sH.get(x, 0) + 1
for x in b:
  sH[x] = sH.get(x, 0) - 1
print(sH)
for x in a: # 키 값들만 i 에 대응
  if sH.get(x) != 0:
    print("NO")
    break
else:
  print("YES")

###########################
# 인프런 기본 답안
# a = input()
# b = input()
# str1 = dict()
# str2 = dict()

# for x in a:
#   str1[x] = str1.get(x, 0) + 1
# for x in b:
#   str2[x] = str2.get(x, 0) + 1
# print(str1)
# print(str2)

# for i in str1.keys(): # 키 값들만 i 에 대응
#   if i in str2.keys():
#     print(i)
#     if str1[i] != str2[i]:
#       print("NO")
#       break
#   else:
#     print("NO")
#     break
# else:
#   print("YES")


##########################
# 시작시간 230929 18:34  마무리시간 18:42
# 딕셔너리 문제라는데 나는 너무 쉬운 다른 방법으로 풀음

# word1 = input()
# li_word1 = []
# for x in word1:
#   li_word1.append(x)
# word2 = input()
# li_word2 = []
# for x in word2:
#   li_word2.append(x)
# li_word1.sort()
# li_word2.sort()

# if (li_word1 == li_word2):
#   print("YES")
# else:
#   print("NO")

#########################
