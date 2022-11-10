# 짝수면 1
def isEven(n):
    if (n ^ 1) == (n + 1):
        return 1
    else:
        return 0
# 
def isEvenUseAnd(n):    
    if (n & 1):
        return 0
    else:
        return 1
n = int(input())
# 짝수면 1
if(isEven(n) == 1):
    print("Even")
else:
    print("Odd")

if(isEvenUseAnd(n) == 1):
    print("Even")
else:
    print("Odd")
