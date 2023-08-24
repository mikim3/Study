# 230824 20:09 20:25

word = input()

length = len(word)

if length % 2 == 0:
  if word[0:length // 2] == word[length - 1:length // 2 - 1:-1]:
    print(1)
  else:
    print(0)
else:
  if word[0:length // 2] == word[length - 1:length // 2:-1]:
    print(1)
  else:
    print(0)

