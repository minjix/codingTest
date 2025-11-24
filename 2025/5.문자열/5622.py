s = input()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sec = 0

for i in range(len(dial)):
    for j in s:
        if j in dial[i]:
            sec += (i + 3)

print(sec)