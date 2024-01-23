from collections import defaultdict

# 기존에 없는 키에 접근시 에러 출력
dic = {}
# 기존에 없는 키 값에 접근하려 할때 기본값으로 ()안에 값을
dic_default = defaultdict(list)
print(dic)
print(dic_default)

times = [[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]]

# error
# for time in times:
#   dic[time[0]].append((time[2],time[1]))
# print(dic)

for time in times:
    if time[0] not in dic:
        dic[time[0]] = []
    dic[time[0]].append((time[2], time[1]))
print('dic == ', dic)


for time in times:
  dic_default[time[0]].append((time[2],time[1]))
print(dic_default)

# value 만 반환
for i in dic_default.values():
  print('values ==',i)
# (key, value) 형태
for i in dic_default.items():
  print('items == ', i)
for i in dic_default.keys():
  print('keys == ', i)
# print(dic_default.clear())
# print(dic_default)


