s = input()

word = list()
num = list()

for i in range(len(s)):
    x = s[i].upper()
    if x not in word:
        word.append(x)
        j = word.index(x)
        num.append(1)
    else:
        j = word.index(x)
        num[j] += 1
    
max_num = max(num)

if num.count(max_num) > 1:
    print('?')
else:
    num_index = num.index(max_num)
    print(word[num_index])

    