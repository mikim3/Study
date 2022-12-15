# 아이디어

# 바로 앞과 바로 뒤를 합치는 경우 두가지 수만 나온다 
# 그 두 수만 합치면 그대로 정렬했을떄 가장큰수를 만들떄 쓸수 있는 경우인지 결정할 수 있다.

# : {10, 68, 75, 7, 21, 12 }

def largestNumber(array):
    if len(array)==1:
        return str(array[0])
    for i in range(len(array)):
        array[i]=str(array[i])
    # [10,68,75,7,21,12]=>[‘10',‘68',‘75',‘7‘,’21’,’12’]
    for i in range(len(array)):
        for j in range(1+i, len(array)):
            if array[j]+array[i]>array[i]+array[j]:
                array[i],array[j]=array[j],array[i]
    #[‘7', ‘75', ‘68', ‘21‘…]
    #Refer JOIN function in Python
    result=''.join(array)
    if(result=='0'*len(result)):
        return '0'
    else:
        return result
#main
# arr = [10, 68, 75, 7, 21, 12]
arr = []
print(largestNumber(arr))
        
        