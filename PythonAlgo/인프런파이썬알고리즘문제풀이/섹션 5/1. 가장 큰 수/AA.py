##########################
# 시작시간     마무리시간

# 본인 앞에 있는게 자기보다 작으면 앞에 있는걸 pop한다.
# m 개를 지울수 있다 == pop핤수 있다.
# 

# 스택에 맨  앞앞과  비교 후 본인보다 작작으으면  pop
# pop 갯수를 다쓰면 그냥 스택에 쌓고 마무리


n,m = map(int,input().split())

n_str = str(n) # 입력받은거 str로 변환
li = [] # 비교할 스택 
# 
ret = ''
li.append(n_str[0]) 
for i in range(1,len(n_str)):
    if (li[-1] < n_str[i]):
        li.pop()
    else:
        li.append(n_str[i]) 

print(li)




#########################
