# 10분걸림

st = input()
st_num = ""

for i in range(len(st)):
    if st[i].isdigit()== True:
        st_num += st[i] 
st_num = int(st_num)

print(st_num)

count = 1
for i in range(1,st_num//2+1):
    if st_num % i == 0:
        count+=1

print(count)

