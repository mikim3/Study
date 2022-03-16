#10828 스택
# 답지봄!!
# 파이썬은 따로 스택구조를 제공안한다고 한다.
# 대신 list.pop() 이 있으니 쉽게 구현가능하다.

import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    command = input().split()
    if (command[0] == 'push'):
        stack.append(command[1])    
    if (command[0] == 'pop'):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if (command[0] == 'size'):
        print(len(stack))
    if (command[0] == 'empty'):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)    
    if (command[0] == 'top'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[-1])


# 9093번 단어뒤집기