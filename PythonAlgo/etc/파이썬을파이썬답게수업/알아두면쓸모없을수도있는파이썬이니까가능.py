
# n 진법으로 표기된 string 을 10진법 숫자로 변환하기 - int 함수
# num, base = map(int, input().strip().split(' '))

# num_s = str(num)
# answer = int(num_s,base)

# print(answer)

# 문자열 정렬하기
### 정렬
# s = 'abc'
# n = 7

# print(s.ljust(n)) # 좌측 정렬
# print(s.center(n)) # 가운데 정렬
# print(s.rjust(n)) # 우측 정렬

# 알파벳 전부 출력하기
# import string 
# num = int(input().strip())

# if num == 0:
#     print(string.ascii_lowercase) # 소문자 abcdefghijklmnopqrstuvwxyz
# else:
#     print(string.ascii_uppercase)
#  # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits

# 파이썬에서의 * 의 역할   
# unpacking 을 해준다.   말뜯 그대로 가장 겉에 괄호를 없앤다고 생각하면 좋다.

li = [1,2,3,4,5,6]
print(*li)  # 1 2 3 4 5 6

tu = (1,2,3,4,5)
print(*tu)




# 2차원배열 뒤집기

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))

#     *mylist == [1,2,3],[4,5,6],[7,8,9]
#   ([1,2,3],[4,5,6],[7,8,9]) <-- zip으로 만들어진 값


print(new_list)

print(mylist)