alpa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

num = 0
for i in range(len(alpa)):
    num += word.count(alpa[i])

print(len(word) - num)
    
    
