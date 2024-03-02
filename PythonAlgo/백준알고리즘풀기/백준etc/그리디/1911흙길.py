###########################
# 시작시간 1708 마무리시간

# N개의 물 웅덩이
# 물웅덩이를 덮을 수 있는 길이가 L

n, l = map(int, input().split())
li = []
for i in range(n):
  li.append(list(map(int,input().split())))

# 그전 널빤지를 덮은게 
# 다음 널빤지를 최대한 덮어야함

print(li)
li.sort(key= lambda x : (x[1]))
print(li)
