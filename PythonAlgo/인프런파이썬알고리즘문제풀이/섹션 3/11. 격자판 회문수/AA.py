# 260208 시작 2115  마무리 2139

# 문제에 그림과 실제 문제 내용이 일치하지 않을수도 있다는 
# 예시를 보여준 뒤통수 문제

li =[]
n = 7 # 배열길이
m = 5 # 회문길이
count = 0
for i in range(n):
    li.append(list(map(int,input().split())))
# 가로만 탐색
for i in range(n):
    for j in range(n-4):
        li_tmp = []
        for z in range(m):
            li_tmp.append(li[i][j+z])
        res = 1
        for z in range(m//2):
            if li_tmp[z] != li_tmp[m-z-1]:
                res = 0
                break
        if res == 1:
            count += 1

for i in range(n-4):
    for j in range(n):
        li_tmp = []
        for z in range(m):
            li_tmp.append(li[i+z][j])
        res = 1
        for z in range(m//2):
            if li_tmp[z] != li_tmp[m-z-1]:
                res = 0
                break
        if res == 1:
            count += 1
print(count)



# 약 12분걸림

# li = []

# for i in range(7):
#     li.append(list(map(int,input().split())))
    
# # 일시적으로 담아서 확인하는 배열
# li_c = []
# num_of = 0
# for i in range(7):
#     for j in range(3):
#         for a in range(5):
#             li_c.append(li[i][a + j])
#         if li_c[0] == li_c[4] and li_c[1] == li_c[3]:
#                 num_of+=1
#         li_c.clear()

# for j in range(7):
#     for i in range(3):
#         for a in range(5):
#             li_c.append(li[i + a][ j])
#         if li_c[0] == li_c[4] and li_c[1] == li_c[3]:
#                 num_of+=1
#         li_c.clear()

# print(num_of)

