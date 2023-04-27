# 스도쿠 검사  11 35  11 50끝

li = []

for i in range(9):
    li.append(list(map(int, input().split())))


now = 0
li_ch = []
fail = "YES"

for i in range(9):
    for j in range(9):
        li_ch.append(li[i][j])
        if len(li_ch) != len(set(li_ch)):
            fail = "NO"
    li_ch.clear()
    
for i in range(9):
    for j in range(9):
        li_ch.append(li[j][i])
        if len(li_ch) != len(set(li_ch)):
            fail = "NO"
    li_ch.clear()
x = 0
y = 0
for y in range(3):
    for x in range(3):
        for i in range(3):
            for j in range(3):
                li_ch.append(li[i+y*3][j+x*3])
                if len(li_ch) != len(set(li_ch)):
                    fail = "NO"
        li_ch.clear()

print(fail)
    