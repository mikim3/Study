n=int(input())
a=-1  # 가장 최근 새로운수 
b=0
count=0
c=0 # 앞에서 구한합
while n!=a:
    if count==0:  # 처음에만 a에 n값대입
        a=n
    if a<10: #만약 10보다 작으면
        a=a*11 
        count+=1
        continue
    else:
        pass
    c=int(str(a)[-1])+int(str(a)[0])  # 각자리의 수를 더한다. 
    a=int(str(a)[-1]+str(c)[-1]) #N의 가장 오른쪽 자리수
    count+=1
print(count)