# 시작 0203 2037 마무리 2107
# 문제를 잘 읽자 약수는 소수가 아니다.

st = input()

num = 0
num_st = ""
count = 0
for i in range(len(st)):
    if st[i].isdigit():
        num_st += st[i] 
num = int(num_st)

for i in range(1,num+1):
    if num % i == 0:
        count+=1 
print(num)
print(count)

# 0502 대충 6분걸림

# word = input()
# make_word = ''
# for i in word:
#     if (i.isdigit()):
#         make_word += i 
# num = int(make_word)

# check = 1
# for i in range(1,num):
#     if (num % i == 0):
#         check += 1
# print(num)
# print(check)

# # 10분걸림

# st = input()
# st_num = ""

# for i in range(len(st)):
#     if st[i].isdigit()== True:
#         st_num += st[i] 
# st_num = int(st_num)

# print(st_num)

# count = 1
# for i in range(1,st_num//2+1):
#     if st_num % i == 0:
#         count+=1

# print(count)

