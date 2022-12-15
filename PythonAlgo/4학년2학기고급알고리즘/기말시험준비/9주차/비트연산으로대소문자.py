## 32차이
# n = int(input())
# print(n^32)
sentence = input() 

for i in range(len(sentence)):
    print(chr(ord(sentence[i])^32),end = '')
    