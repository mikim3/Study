#

n,b=list(map(str,input().split()))
b = int(b)
sum = 0
def this_num(a):
    if ord('A') <= ord(a) <= ord('Z'):
        a = ord(a) - ord('A') + 10
    else:
        a = int(a)
    return a;
j = len(n) - 1
for i in n:
    sum += (b ** j) * this_num(i) 
    j-=1
# print()

# for i in n:
#     print(this_num(i))

print(sum)


