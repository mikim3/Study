# 시작시간 2330
# 0040에 답봄    

# 숫자 있으면 괄호값 * 숫자값

# 옆에 나열돼 있으면 +
# 안에 들어가 있으면 곱하기계산해야함

# 올바르지 못하면 0 출력

in_value = input()  # 입력값 받기
stack = []          # 괄호를 저장할 스택
result = 0          # 최종 결과 값
temp = 1            # 괄호의 값을 계산하기 위한 임시 변수

for i in range(len(in_value)):  # 문자열의 각 문자 검사
    char = in_value[i]

    if char == '(':
        stack.append(char)  # '('를 스택에 추가
        temp *= 2           # '('는 값이 2로 곱해져야 하므로 temp에 2를 곱함
    elif char == '[':
        stack.append(char)  # '['를 스택에 추가
        temp *= 3           # '['는 값이 3으로 곱해져야 하므로 temp에 3을 곱함
    elif char == ')':
        # 닫는 괄호 ')'가 올 때:
        if not stack or stack[-1] != '(':
            # 스택이 비어 있거나 짝이 맞지 않으면 올바르지 않은 괄호열
            result = 0
            break
        if in_value[i - 1] == '(':
            # 직전 문자가 '('라면 temp 값을 result에 더함
            result += temp
        stack.pop()  # '('를 스택에서 제거
        temp //= 2   # '('에 대한 값을 제거하므로 temp에서 2를 나눔
    elif char == ']':
        # 닫는 괄호 ']'가 올 때:
        if not stack or stack[-1] != '[':
            # 스택이 비어 있거나 짝이 맞지 않으면 올바르지 않은 괄호열
            result = 0
            break
        if in_value[i - 1] == '[':
            # 직전 문자가 '['라면 temp 값을 result에 더함
            result += temp
        stack.pop()  # '['를 스택에서 제거
        temp //= 3   # '['에 대한 값을 제거하므로 temp에서 3을 나눔
    else:
        # 잘못된 문자가 들어온 경우
        result = 0
        break

# 반복문이 끝난 후 스택이 비어 있지 않으면 올바르지 않은 괄호열
if stack:
    result = 0

print(result)  # 결과 출력
