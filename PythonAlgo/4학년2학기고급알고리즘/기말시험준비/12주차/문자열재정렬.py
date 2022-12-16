# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
st = input()
arr_st= []
arr_num = []

for i in range(len(st)):
    if '0' <= st[i] <= '9':
        arr_num.append(int(st[i]))
    else:
        arr_st.append(st[i])
arr_st.sort()
for i in range(len(arr_st)):
    print(arr_st[i],end='')

print(sum(arr_num))