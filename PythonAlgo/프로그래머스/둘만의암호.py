
def solution(s, skip, index):
  answer = ''
  for char in s:
    move_count = 0
    ascii_val = ord(char)
    while move_count < index:
      ascii_val += 1
      if ascii_val > ord('z'):
        ascii_val = ord('a')
      if chr(ascii_val) not in skip:
        move_count += 1
    answer += chr(ascii_val)
  return answer

########### 우진이소스
# def solution(s, skip, index):
#   answer = ""
  
#   for char in s:
#     # alpha_i는 char가 몇번째 알파벳인지를 알려주는 값이 됨
#     alpha_i = ord(char) - ord('a')

#     d = 0
#     while d < index:
#       alpha_i = (alpha_i + 1) % 26
#       if chr(alpha_i + ord('a')) not in skip:
#         d += 1
#     answer += chr(alpha_i + ord('a'))
#   return answer
###########

print(solution("aukks", "wbqd", 5)) # happy