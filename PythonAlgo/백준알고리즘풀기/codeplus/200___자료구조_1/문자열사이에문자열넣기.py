
str_a = "안녕하세요 {}입니다.".format("독학코딩")
print(str_a)

str_a = "안녕하세요 {}입니다. 오늘은 {}을 배워보겠습니다.".format("독학코딩", "Python")
print(str_a)

str_a = "안녕하세요 {name}입니다. 오늘은 {title}을 배워보겠습니다.".format(title="Python", name="독학코딩")
print(str_a)

str_a = "안녕하세요 %s입니다." % "독학코딩"
print(str_a)

str_a = "안녕하세요 %s입니다. 오늘은 %s을 배워보겠습니다." % ("독학코딩", "Python")
print(str_a)

str_a = "안녕하세요 입니다."
index = str_a.find("입니다")
str_b = str_a[:index] + '독학코딩' + str_a[index:]
print(str_b)

str_a = "안녕하세요 입니다."
list_a = str_a.split()
list_a.insert(list_a.index("입니다."), '독학코딩')
str_b = ' '.join(list_a)
print(str_b) ## 방법만 결과가 조금 다릅니다. 유의 하셔야 합니다.

str_b = "독학코딩"
str_a = f"안녕하세요 {str_b}입니다."
print(str_a)
