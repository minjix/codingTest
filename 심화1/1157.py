# 선언하는 쪽 간단하게 바꿀 수 있게 다시 보기!
word = list(str(input()).upper())
new = list(set(word))

num = []
for i in range(len(new)):
    num.append(word.count(new[i]))

nMax = max(num)

if num.count(nMax) > 1:
    print("?")
else:
    i = num.index(nMax)
    print(new[i])

