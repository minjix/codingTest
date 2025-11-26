s = input()

l = len(s)
x = len(s) // 2

if l % 2 == 0:
    #이것도 됨
    #y = s[x:]
    #print(y[::-1])
    if s[:x] == ''.join(reversed(s[x:])):
        print(1)
    else:
        print(0)
else:
    if s[:x] == ''.join(reversed(s[x+1:])):
        print(1)
    else:
        print(0)

