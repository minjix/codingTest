S = input()

num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

ret = 0
for i in range(len(S)):
    for j in num:
        if S[i] in j:
            ret += num.index(j)+3

print(ret)