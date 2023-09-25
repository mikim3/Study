##########################
# 시작시간 21:27    마무리시간 21:33

n = int(input())
li = []

for i in range(n):
  li.append(input())

for i in range(n-1):
  input_word = input()
  if input_word in li:
    li.remove(input_word)

print(li[0])

#########################
