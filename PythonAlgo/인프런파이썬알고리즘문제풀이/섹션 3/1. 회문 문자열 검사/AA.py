# 시작 260203 2022 마무리 2036

n = int(input())
for i in range(n):
    st = input()
    st = st.upper()
    if len(st) % 2 == 1:
        st = st[:len(st)//2] + st[len(st)//2+1:]
    lp = 0
    rp = len(st)-1
    y_n = "YES" # yes
    while lp < rp: #
        if st[lp] != st[rp]:
            y_n = "NO"
            break 
        lp += 1
        rp -= 1
    print(f"#{i+1} {y_n}")


# 0502 20:44 시작시간  20:57마무리
# upper는 알았는데 lower를 몰라서 서칭함
# sys input 썼을때 strip() 써야되는거 서칭으로 알음

# import sys
# input = sys.stdin.readline

# n = int(input().strip())

# def reverse_word(input_word):
#     reversed_word = ''
#     for i in input_word:
#         reversed_word = i + reversed_word
#     return reversed_word

# for i in range(n):
#     input_word = input().strip().lower()
#     if (input_word == reverse_word(input_word)):
#         print("#" + str(i+1) + "YES")
#     else:
#         print("#" + str(i+1) + "NO")


# # 21 33  5 +  22 00    
# # 16분걸림
# import sys
# input = sys.stdin.readline

# n = int(input())

# for i in range(n):
#     li = list(map(str,input().rstrip()))
#     li_r =  []
    
#     li_r = list(reversed(li))
    
#     li = "".join(li)    
#     li_r = "".join(li_r)

#     li = li.upper()
#     li_r = li_r.upper()
#     if li == li_r:
#         print("#%d YES"%(i+1))
#     else:
#         print("#%d NO"%(i+1))
    



    
    

