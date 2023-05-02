# 0502 대충 6분걸림

word = input()
make_word = ''
for i in word:
    if (i.isdigit()):
        make_word += i 
num = int(make_word)

check = 1
for i in range(1,num):
    if (num % i == 0):
        check += 1
print(num)
print(check)

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

