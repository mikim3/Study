# 모든 비트 자리수에 a[i] ^= 32 하면 홀짝 바뀜

def toggleCase(st):
    st_li = list(st)
    temp = 0
    for i in range(len(st_li)):
        temp = ord(st_li[i]) ^ 32
        st_li[i] = chr(temp)
        # print(st_li)s
    st = ''.join(st_li)
    return st;
st = input()
print(toggleCase(st))
