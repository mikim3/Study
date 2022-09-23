# total = total + s[i+1] 이 부분을 total += s[i] + s[i+1] 로 입력해서 오래 걸렸다.


# 02984 --> ((((0 + 2) × 9) × 8) × 4) = 576
s = list(map(int,input()))
print(s)
li_select = []
for i in range(len(s) - 1):
    if s[i] == 0 or s[i] == 1:
        li_select.append(0)
    else:
        li_select.append(1)
total = 0
# print(li_select)
for i in range(len(li_select)):
    if li_select[i] == 0:
        total = total + s[i+1]
    else:
        total = total * s[i+1]
    # print(total)
print(total)

