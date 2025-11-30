cro = ['c=', 'c-', 'dz=', 'd-','lj', 'nj', 's=', 'z=']

s = input()
cnt = 0
t = ''

for i in cro:
    s = s.replace(i, "*")

print(len(s))