# 약 12분걸림

li = []

for i in range(7):
    li.append(list(map(int,input().split())))
    
# 일시적으로 담아서 확인하는 배열
li_c = []
num_of = 0
for i in range(7):
    for j in range(3):
        for a in range(5):
            li_c.append(li[i][a + j])
        if li_c[0] == li_c[4] and li_c[1] == li_c[3]:
                num_of+=1
        li_c.clear()

for j in range(7):
    for i in range(3):
        for a in range(5):
            li_c.append(li[i + a][ j])
        if li_c[0] == li_c[4] and li_c[1] == li_c[3]:
                num_of+=1
        li_c.clear()

print(num_of)

