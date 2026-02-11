# 260208 시작 2015 마무리 2050

n = 9
li = []
res = 1 # YES 
for i in range(n):
    li.append(list(map(int,input().split())))

for i in range(n):
    li_tmp = [x for x in li[i]]        
    li_tmp.sort()
    for j in range(n-1):
        if li_tmp[j]== li_tmp[j+1]:
            res = 0
            break
# print("tt",li[0:9][0:3])
for i in range(n): # 열
    # li_tmp = [x for x in li[0:9][i]]
    li_tmp =[]
    for j in range(n):
        li_tmp.append(li[j][i])
    # print(li_tmp)
    li_tmp.sort()
    for j in range(n-1):
        if li_tmp[j]==li_tmp[j+1]:
            res = 0
            break
for i in range(3):
    for j in range(3):
        li_tmp = []
        for x in range(i*3,i*3+3):
            for y in range(j*3,j*3+3):
                li_tmp.append(li[x][y])
        li_tmp.sort()
        for z in range(n-1):
            if li_tmp[z] == li_tmp[z+1]:
                res = 0
                break
if res == 1:
    print("YES")
else:
    print("NO")


# 스도쿠 검사  11 35  11 50끝

# li = []

# for i in range(9):
#     li.append(list(map(int, input().split())))


# now = 0
# li_ch = []
# fail = "YES"

# for i in range(9):
#     for j in range(9):
#         li_ch.append(li[i][j])
#         if len(li_ch) != len(set(li_ch)):
#             fail = "NO"
#     li_ch.clear()
    
# for i in range(9):
#     for j in range(9):
#         li_ch.append(li[j][i])
#         if len(li_ch) != len(set(li_ch)):
#             fail = "NO"
#     li_ch.clear()
# x = 0
# y = 0
# for y in range(3):
#     for x in range(3):
#         for i in range(3):
#             for j in range(3):
#                 li_ch.append(li[i+y*3][j+x*3])
#                 if len(li_ch) != len(set(li_ch)):
#                     fail = "NO"
#         li_ch.clear()

# print(fail)
    