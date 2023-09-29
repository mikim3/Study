##########################
# 시작시간 230929 14:18    마무리시간 14:51
# 문법적으로 더 쉬운 방법이 있을꺼라는 예상은 들지만 일단 되는데로 풀음


required_str = input()
required = list()
for x in required_str:
  required.append(x)
n = int(input())

for i in range(n):
  required_tmp = required.copy()
  tmp = input()
  li = []
  for x in tmp:
    li.append(x)
  j = 0
  while li:
    # 필수과목 안에 있으면
    if li[j] in required_tmp:
      if li[j] == required_tmp[0]:
        required_tmp.remove(li[0])
        li.remove(li[j])
      else:
        print(f"#{i+1} NO")
        break
    else:
      li.remove(li[j])
    if li == []:
      if required_tmp == []:
        print(f"#{i+1} YES")
      else:
        print(f"#{i+1} NO")
      
#########################
