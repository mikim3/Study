
# 곱하기 혹은 더하기문제
# 문제 : 각자리 0~9까지의 수만 0134532 이런식으로 입력할때 + X 만으로 가장 큰수가 나오도록 계산하도록 하여라

# 0과1은 더하고 나머지수는 곱하는게 핵심
# data = input()

# # 첫 번째 문자를 숫자로 변경하여 대입 
# result = int(data[0])   # 왜 첫번째는 대입한다는 생각을 왜 못 했을까

# for i in range(1,len(data)):
#     # 두 수 중에서 하나라도 ''
#     num = int(data[i])
#     if num <= 1 or result <=1:
#         result += num
#     else:
#         result *= num
        
# print(result)